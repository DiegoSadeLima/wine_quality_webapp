#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[ ]:


import os
import pickle
import pandas as pd
from flask import Flask, request

from wine_quality.WineQuality import WineQuality

#load model
#model = pickle.load(open('model_wine_quality.pkl', 'rb'))

#instanciate flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict():
    model = pickle.load(open('model/model_wine_quality.pkl', 'rb'))
    test_json = request.get_json()
    
    # collect data 
    if test_json:
        if isinstance(test_json, dict): #unique value
            df_raw = pd.DataFrame(test_json, index=[0])
        else:
            df_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
    
    #Instanciate data preparation
    pipeline = WineQuality()
    
    # data preparation
    df1 = pipeline.data_preparation(df_raw)
    
    
    #prediction
    pred = model.predict(df1)
    
    df_raw['prediction'] = pred
    
    return df_raw.to_json(orient='records')
           
if __name__ == '__main__':
    #start flask
    port = os.environ.get('PORT','5000')
    app.run(host='0.0.0.0', port=port) 


# In[ ]:




