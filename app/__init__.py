from flask import Flask
from config import Config

app=Flask(__name__)

app.debug=True
from app import routes