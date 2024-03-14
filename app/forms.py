from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    image = FileField('Photo', validators=[
        FileRequired(message="Please select an image."),
        FileAllowed(['jpg', 'jpeg', 'png'], message="Images Only!")
    ])