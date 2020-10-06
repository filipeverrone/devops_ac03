import os
from flask import Flask, jsonify, request


def eh_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


app = Flask(__name__)

@app.route('/')
def show_cem_primos():
    limit = 100
    primos_showed = 0
    n = 3
    primos = '2, '
    while primos_showed < limit:
        if eh_primo(n):
            primos += str(n) + ', '
            n += 1
            primos_showed += 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
