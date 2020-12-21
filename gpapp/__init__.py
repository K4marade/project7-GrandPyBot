from config import GOOGLE_API_KEY
from flask import Flask

app = Flask(__name__)
app.config['GOOGLE_API_KEY'] = GOOGLE_API_KEY

from . import views
