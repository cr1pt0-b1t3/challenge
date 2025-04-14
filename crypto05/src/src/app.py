from flask import Flask, request, jsonify, current_app
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import datetime
import json

app = Flask(
    __name__,
    static_url_path="",
    static_folder="./static",
    template_folder="./templates",
)


def fake_decode(x):
    return f"{x}"[2:-1]


KEY = b"\xd9\x89\xb4,%p\xa1\xfd|\xea\xe3\xea\xe3\x93\x88\xa8"
flag = "ITASEC{ECB_cu7_4nd_p4573_n3v3r_6375_0ld}"


def register(username):
    if username == "Amministratore":
        return "Questo username non è valido!"
    token = {"username": username, "registration_date": str(datetime.date.today())}
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted_token = cipher.encrypt(pad(json.dumps(token).encode(), 16)).hex()
    return encrypted_token


def login(token):
    try:
        cipher = AES.new(KEY, AES.MODE_ECB)
        token = bytes.fromhex(token)
        decrypted_token = json.loads(unpad(cipher.decrypt(token), 16))
        message = f"Login effettuato con utente {decrypted_token['username']}, registrato in data {decrypted_token['registration_date']}."
        if decrypted_token["username"] == "Amministratore":
            message += f" Ecco la tua flag: {flag}."
        return message
    except Exception as e:
        print(e)
        return "Questo token non sembra valido!"


functions = {
    "register": register,
    "login": login,
}


@app.get("/")
def index():
    return current_app.send_static_file("index.html")


@app.post("/execute")
def execute():
    body = request.json
    print(body)
    if body is None or "fn" not in body or "inputs" not in body:
        return "Missing function or inputs", 400

    fn = body["fn"]
    if fn not in functions:
        return "Function not found", 400

    inputs = body["inputs"]

    try:
        result = functions[fn](*inputs)
        return jsonify({"result": result})
    except Exception as e:
        return str(e), 400


@app.cli.command("install")
def install():
    # Use this to init the database/application.
    # This function will be run on a single thread before launching the server web
    pass
