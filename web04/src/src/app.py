import base64
import json
import os

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

FLAG = os.getenv('FLAG')
USERS = {
    'admin': f'I am confident no one will read this: {FLAG}'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    username = request.args.get('username')
    content = request.args.get('content')

    if not username or not content:
        return 'Invalid username or content'

    if username in USERS:
        return 'User already exists'

    if len(content) > 1024:
        return 'Content too long'

    USERS[username] = content

    r = make_response('Note created')
    r.set_cookie('user', base64.b64encode(json.dumps({'username': username}).encode()).decode())
    return r


@app.route('/get')
def get():
    user = request.cookies.get('user')
    if not user:
        return 'Missing cookie'

    try:
        user = base64.b64decode(user).decode()
        user = json.loads(user)
        user = user.get('username')
    except Exception as e:
        return f'Invalid cookie: {e}'

    if user not in USERS:
        return f'Unknown user: {user}'

    return 'OK: ' + USERS[user]


if __name__ == "__main__":
    app.run(debug=True)
