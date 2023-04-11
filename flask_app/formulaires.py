from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField , RadioField, FileField


class ImgForm(FlaskForm):
    img = FileField("Image en jpeg ou jpg:")
    url = StringField("Url de l'image :", render_kw={"placeholder": "https://images.pexels.com/photos/8451490/pexels-photo-8451490.jpeg"})