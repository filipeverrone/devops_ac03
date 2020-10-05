'''
Faça um programa em python que exiba os 100 primeiros numeros primos
'''

import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')


def eh_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def show_cem_primos():
    limit = 100
    primos_showed = 0
    n = 1
    while primos_showed < limit:
        if eh_primo(n):
            print(n,end=", ")
            n += 1
            primos_showed += 1
    return


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port)
