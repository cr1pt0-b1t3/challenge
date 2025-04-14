from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import sys

ALLOWED_EXTENSIONS = {'txt', 'tar.gz'}

app = Flask(__name__)

def allowed_file(filename):
    return any(filename.endswith('.' + extension) for extension in ALLOWED_EXTENSIONS)

@app.route('/', methods=['GET'])
def upload_form():
    return '''
    <!doctype html>
    <html>
    <head>
        <title>Upload new File</title>
    </head>
    <body>
        <h2>Upload new File</h2>
        <form method=post enctype=multipart/form-data action="/upload">
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>   
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        return jsonify({'message': 'File successfully uploaded'}), 200
    else:
        return jsonify({'error': 'Wrong file type'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
