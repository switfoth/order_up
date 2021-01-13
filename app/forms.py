from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, SubmitField)
from wtforms.validators import DataRequired

v = [DataRequired()]


class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", v)
    password = PasswordField("Password", v)
    submit = SubmitField("Login")
