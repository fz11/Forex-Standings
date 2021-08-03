from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flaskwebsite.model import User

class ContactForm(FlaskForm):
    name = StringField("Your Name:", validators=[DataRequired(), Length(min=1, max=30)])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    message = StringField("Your Message Here:", validators=[DataRequired()])
    submit_form = SubmitField("Submit")



