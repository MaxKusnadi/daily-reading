import logging

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


logging.basicConfig(level=logging.INFO,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config.from_object('config')
CORS(app)
db = SQLAlchemy(app)

# Views
from app.view import *

# Models
from app.model import *
