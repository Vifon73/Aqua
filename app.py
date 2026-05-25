import base64
import secrets
import string
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def encoding(text):
    res = ""
    salt = "aquA"
    # odwróć na początek
    reverse = text[::-1]

    for char in reverse:
        if char.isalpha():
            if char.isupper():
                res += chr((ord(char) - ord('A') + 67) % 26 + ord('A'))
            else:
                res += chr((ord(char) - ord('a') + 67) % 26 + ord('a'))
        else:
            res += char

    # daj sól na koniec
    res += salt
    return base64.b64encode(res.encode()).decode()


def decoding(text):
    salt = "aquA"
    res = ""
    # dekoduj base64
    decoded = base64.b64decode(text).decode()
    # usuń sól
    without_salt = decoded[:-len(salt)]

    for char in without_salt:
        if char.isalpha():
            if char.isupper():
                res += chr((ord(char) - ord('A') - 67) % 26 + ord('A'))
            else:
                res += chr((ord(char) - ord('a') - 67) % 26 + ord('a'))
        else:
            res += char

    # odwróć z powrotem
    return res[::-1]


def generate_password(typ, dlugosc):
    # wybierz zestaw znaków
    if typ == "digits":
        znaki = string.digits
    elif typ == "letters":
        znaki = string.ascii_letters
    else:
        znaki = string.digits + string.ascii_letters

    # losuj znaki
    password = ""
    for _ in range(dlugosc):
        password += secrets.choice(znaki)
    return password


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/encode", methods=["POST"])
def encode_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Brak tekstu"}), 400

    result = encoding(text)
    return jsonify({"result": result})


@app.route("/decode", methods=["POST"])
def decode_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Brak tekstu"}), 400

    try:
        result = decoding(text)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": "Błąd przy dekodowaniu"}), 400


@app.route("/password", methods=["POST"])
def password_route():
    data = request.get_json()
    typ = data.get("type", "mixed")
    dlugosc = data.get("length", 16)

    # waliduj długość
    try:
        dlugosc = int(dlugosc)
    except ValueError:
        return jsonify({"error": "Nieprawidłowa długość"}), 400

    if dlugosc < 1 or dlugosc > 128:
        dlugosc = 16

    haslo = generate_password(typ, dlugosc)
    return jsonify({"result": haslo})


if __name__ == "__main__":
    app.run(debug=True)