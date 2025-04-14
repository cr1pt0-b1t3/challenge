from flask import Flask, request, jsonify, current_app

app = Flask(
    __name__,
    static_url_path="",
    static_folder="./static",
    template_folder="./templates",
)


def fake_decode(x):
    return f"{x}"[2:-1]

flag = b"ITASEC{0n3_by73_m4yb3_15_700_l4zy_f0r_4_k3y}"
secret_char = '['

def get_encrypted_flag():
    return minimal_xor(hex_encode(flag), secret_char)

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

def minimal_xor(hex_string, char):
    message = hex_decode(hex_string)
    return hex_encode(
        bytes([message[i] ^ ((ord(char) + i) % 256) for i in range(len(message))])
    )


functions = {
    "get_encrypted_flag": get_encrypted_flag,
    "hex_encode": lambda x: hex_encode(x.encode()),
    "hex_decode": lambda x: fake_decode(hex_decode(x)),
    "minimal_xor": lambda x, y: minimal_xor(x, y),
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
