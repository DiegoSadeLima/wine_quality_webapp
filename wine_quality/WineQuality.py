#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


import pickle

class WineQuality(object):
    def __init__(self):
        self.free_sulfur_scaler = pickle.load(open("parameter/free_sulfur_scaler.pkl","rb"))
        self.total_sulfur_scaler = pickle.load(open("parameter/total_sulfur_scaler.pkl","rb"))
        
    def data_preparation(self, df):
        
        df["free sulfur dioxide"] = self.free_sulfur_scaler.transform(df[["total sulfur dioxide"]].values)
        
        df["total sulfur dioxide"] = self.total_sulfur_scaler.transform(df[["total sulfur dioxide"]].values)
        
        return df   


# In[ ]:




