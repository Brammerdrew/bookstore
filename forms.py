from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserSignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email')])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()