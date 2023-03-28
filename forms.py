from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    userName = StringField('Full name:', [DataRequired()])
    email = EmailField('Email:', [DataRequired()])
    password1 = PasswordField('Password:', [DataRequired()])
    password2 = PasswordField('Repeat pass:', [DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email:', [DataRequired()])
    password = PasswordField('Password:', [DataRequired()])
    submit = SubmitField('Login')
    
class AddGroup(FlaskForm):
    groupId = StringField('Group ID:', [DataRequired()])
    submit = SubmitField('Add')
    
class Bills(FlaskForm):
    amout = StringField('Amout:', [DataRequired()])
    discription = StringField('Discription:', [DataRequired()])
    groupid = StringField('', [DataRequired()])
    submit = SubmitField('Add')