import os
from flask import Flask, render_template, redirect, url_for, request, session
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt, mpld3
from ultralytics import YOLO
import numpy as np
import requests
from formulaires import ImgForm

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('SECRET_KEY')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Route pour la page d'accueil
@app.route('/',methods=['GET','POST'])
def accueil():
    form = ImgForm()
    if form.validate_on_submit():
        img_file = request.files['img']
        image = Image.open(img_file)
        image = np.asarray(image)
        model = YOLO('./best.pt')
        result = model.predict(source=image,classes = None)

        fig, ax = plt.subplots()
        ax.imshow(result[0].plot(img=image))
        
        htmlimg = mpld3.fig_to_html(fig)

        return render_template('index.html',form=form,image=htmlimg)



    return render_template('index.html',form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()