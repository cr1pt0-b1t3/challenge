import os

from flask import Flask, make_response, render_template

app = Flask(__name__)

FLAG = os.getenv('FLAG')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logo.svg')
def logo():
    with open('logo.svg', 'r') as f:
        data = f.read()

    data = data.replace('FLAG_HERE', FLAG)

    r = make_response(data)
    r.headers['Content-Type'] = 'image/svg+xml'
    return r


if __name__ == "__main__":
    app.run(debug=True)
