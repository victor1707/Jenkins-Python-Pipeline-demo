# app.py
from flask import Flask 
import os 
app = Flask(__name__) 
@app.route('/')

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def hello(): 
    return ('\nHello from Container World!-Deployment using Docker Image \n\n')


if __name__ == "__main__":
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    app.run(host="0.0.0.0", port=8080, debug=True)

