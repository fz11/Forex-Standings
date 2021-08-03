from datetime import datetime
from flaskwebsite import db

class User(db.Model):
    uniqueid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False, default="")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return "({name}, {email}, {message}, at {date})".format(name=self.name, email=self.email, message=self.message, date=self.date_posted)

