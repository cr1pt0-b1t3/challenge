import base64
import os

from flask import Flask, render_template

app = Flask(__name__)

FLAG = os.getenv('FLAG')


@app.route('/')
def index():
    data = {}

    i, j, k = 0, len(FLAG) - 1, False
    while j - i >= 0:
        data[j - i] = FLAG[i if k else j]
        if k:
            i += 1
        else:
            j -= 1
        k = not k

    data = base64.b64encode(''.join([data[i] for i in range(max(data.keys()) + 1)]).encode()).decode()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
