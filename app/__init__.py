from flask import Flask

app = Flask(__name__)

from app import routes  # import after app is created to avoid circular import
