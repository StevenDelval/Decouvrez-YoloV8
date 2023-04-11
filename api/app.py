from fastapi import FastAPI, HTTPException
import numpy as np
from io import BytesIO
from PIL import Image
from ultralytics import YOLO
import requests

app = FastAPI()

@app.post("/predict")
async def process_array(image):
    image = np.array(image)
    model = YOLO('./best.pt')
    result = model.predict(source=image,classes = None)
    return result[0].plot(img=image)

@app.post("/predicturl")
async def process_array(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = np.asarray(image)
    model = YOLO('./best.pt')
    result = model.predict(source=image,classes = None)
    return{"predict" : result[0].plot(img=image).tolist()}