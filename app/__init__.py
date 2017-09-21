import logging

from flask import Flask
from flask_cors import CORS


logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
CORS(app)

# Views
from app.view import *
