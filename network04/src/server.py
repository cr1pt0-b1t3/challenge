import os
import sys
from flask import Flask, request, session, render_template

app = Flask(__name__)
app.secret_key = '242ab46e4cce601548b100b9dfc041961b2d'

FLAG = os.environ.get("FLAG", "ITASEC{redacted}")

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/step1', methods=['GET'])
def endpoint1():
    session['step'] = 1
    return 'okay! first step done.'

@app.route('/step2', methods=['POST'])
def endpoint2():
    if session.get('step') == 1 and request.form.get('hello') == 'world' and request.form.get('dead') == 'beef':
        session['step'] = 2
        return 'correct! go on!'
    else:
        return ':( try again!'

@app.route('/step3', methods=['PUT'])
def endpoint3():
    if session.get('step') == 2:
        session['step'] = 3
        return 'one last step!'
    else:
        return ':( try again!'
    
@app.route('/step4', methods=['DELETE'])
def endpoint4():
    if session.get('step') == 3:
        return f'You did it! The flag is {FLAG}'
    else:
        return ':( try again!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
