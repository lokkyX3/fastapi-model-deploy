from fastapi import FastAPI
import tensorflow as tf
from tensorflow import keras
import json
import numpy as np
import requests


app = FastAPI()

model = tf.keras.models.load_model('/model/loan_prediction.h5')

def get_prediction(client):
    x = client.values.reshape(1,80)
    y = model.predict_classes(x)
    return {'prediction': y}


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/predict-post/")
def post_predict():
    try:
      client_data = requests.json
      pred = get_prediction(client_data)
      return pred

    except Exception as e:
      print(e)

