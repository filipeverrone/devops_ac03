import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def show_primos():
    limit = 100
    primos_showed = 1
    n = 3
    primos = '2, '
    while primos_showed < limit:
        ehPrimo = True
        for i in range(2, n):
            if n % i == 0:
                ehPrimo = False
                break
        if ehPrimo:
            primos = primos + str(n) + ', '
            n += 1
            primos_showed += 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
