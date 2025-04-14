from flask import Flask, request, jsonify, current_app
from sympy.ntheory.modular import crt

app = Flask(
    __name__,
    static_url_path="",
    static_folder="./static",
    template_folder="./templates",
)


def fake_decode(x):
    return f"{x}"[2:-1]


flag = b"ITASEC{n07_50_53cr37_5h4r1n6_:(}"
assert len(flag) == 32

primes = [
    690909282108739,
    702862391767649,
    739314349693453,
    784627120326557,
    851891142565129,
    862496600114951,
]


def get_flag_shares():
    flag_int = int.from_bytes(flag, "big")
    shares = [flag_int % p for p in primes]
    return shares[:-1]


def share_your_secret(text):
    if len(text) > 36:
        return "Questo segreto è troppo grande!"
    text_int = int.from_bytes(text, "big")
    shares = [text_int % p for p in primes]
    return shares


def recover_secret(shares):
    if len(shares) != 6:
        return b"Per recuperare un segreto mi servono tutte e 6 le parti!"
    try:
        recovered = int(crt(primes, shares)[0])
        return int.to_bytes(recovered, recovered.bit_length() // 8 + 1, byteorder="big")
    except Exception as e:
        print(e)
        return b"Questo segreto non sembra recuperabile!"


functions = {
    "get_flag_shares": get_flag_shares,
    "share_your_secret": lambda x: share_your_secret(x.encode()),
    "recover_secret": lambda x: fake_decode(recover_secret(list(map(int, x.split(","))))),
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
