from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# __name__ = name of module __main__
app = Flask(__name__)
# relative path from current file.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "93eb09875356e1c1aa709a607841d2a8f84fb41f"
db = SQLAlchemy(app)

from flaskwebsite import routing
