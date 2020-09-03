# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:25:08 2020

@author: Abhishek
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
#def home():
    #return render_template('index.html')
def index_page():
    print(model)
    return render_template('index.html')    

@app.route('/predict', methods=['POST', 'GET'])
#def predict():
def predict_logic():    
    
    if request.method == 'POST':
        acousticness = float(request.form.get('acousticness'))
        danceability = float(request.form.get('danceability'))
        energy = float(request.form.get('energy'))
        instrumentalness = float(request.form.get('instrumentalness'))
        liveness = float(request.form.get('liveness'))
        speechiness = float(request.form.get('speechiness'))                  
        tempo = float(request.form.get('tempo'))
        valence = float(request.form.get('valence'))
    
    pred_name = model.predict([[acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence]]).tolist()[0]
    return render_template('index.html', pred_name=pred_name)
    

   #return render_template('index.html', prediction_text='Music Genre {}'.format(pred_name))


if __name__ == "__main__":
    app.run(debug=True)