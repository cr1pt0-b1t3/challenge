from flask import Flask, request, jsonify, current_app
import datetime
import random

app = Flask(
    __name__,
    static_url_path="",
    static_folder="./static",
    template_folder="./templates",
)


def fake_decode(x):
    return f"{x}"[2:-1]


flag = b"ITASEC{m4yb3_60_k3y5_4r3_n07_3n0u6h...}"

def get_encrypted_flag():
    return temporal_xor(hex_encode(flag))


def hex_encode(s):
    return s.hex()


def hex_decode(h):
    return bytes.fromhex(h)

def xor_tool(s1, s2):
    m1 = bytes.fromhex(s1)
    m2 = bytes.fromhex(s2)
    return hex_encode(
        bytes([m1[i] ^ m2[i] for i in range(min(len(m1), len(m2)))])
    ) 

def temporal_xor(hex_string):
    message = hex_decode(hex_string)
    random.seed(datetime.datetime.now().minute)
    return hex_encode(
        bytes([message[i] ^ random.randint(1,255) for i in range(len(message))])
    )


functions = {
    "get_encrypted_flag": get_encrypted_flag,
    "hex_encode": lambda x: hex_encode(x.encode()),
    "hex_decode": lambda x: fake_decode(hex_decode(x)),
    "temporal_xor": lambda x: temporal_xor(x),
    "xor_tool": lambda x, y: xor_tool(x, y)
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
