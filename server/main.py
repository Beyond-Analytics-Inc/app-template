import requests
import os
from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def index():
    return ('Server running', 200)

if __name__ == '__main__':
    PORT = int(os.getenv('PORT')) if os.getenv('PORT') else 8080
    app.run(host='0.0.0.0', port=PORT, debug=True)