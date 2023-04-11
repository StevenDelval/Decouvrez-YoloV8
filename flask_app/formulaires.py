from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField , RadioField, FileField


class ImgForm(FlaskForm):
    img = FileField("Image a analyser :")