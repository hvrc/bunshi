from flask import Flask
from config import Config

# Create and configure an instance of the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# ?
from . import home
