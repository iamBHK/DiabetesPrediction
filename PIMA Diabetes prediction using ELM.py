# -*- coding: utf-8 -*-
"""ELM_for_PIMA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o7FKoxutx5GAHYu5eDdczMXlC_NUJxBA
"""

!pip install elm
!pip install pandas

import elm
import elm as ELM
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import pandas as pd
import seaborn as sns
import time
import pickle
from keras.models import Sequential
from keras.models import model_from_json
from keras.callbacks import TensorBoard
from keras import optimizers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from numpy import matrix
from sklearn.metrics import accuracy_score

data = pd.read_csv ('diabetes.csv',encoding='utf-8')
X =data[['Pregnancies',	'Glucose'	,'BloodPressure',	'SkinThickness',	'Insulin',	'BMI',	'DiabetesPedigreeFunction'	,'Age',	'Outcome']]
x=X
# x = matrix(data)
foo = sns.heatmap(x.corr(), vmax=1, square=True, annot=True)
plt.figure(figsize=(64,64))
x=x.to_numpy()
y= data[['Outcome']] # 2D
y=y.to_numpy()
t1=y.shape[0]
y=np.reshape(y,(t1,))  # 2D
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.02)

print(x)

dim=x.shape[1]
self=dim

print(self)

hiddenSize=1

weight = np.matrix(np.random.uniform(-0.5, 0.5, (1, dim)))

print(weight)

bias = np.matrix(np.random.uniform(0, 1, (1, 1)))

print(bias)

sigmoid=1 / (1 + np.exp(-1 * x))
print(sigmoid)

class ELM:
    elmk = elm.ELMKernel()
    
    def __init__(self, hidden_layers = 500) -> None:
        self.hidden_layers = hidden_layers
        
    @staticmethod
    def _relu(x):
        return np.maximum(x,0,x)

    def _init_weights(self, X_size):
        self._input_weights = np.random.normal(size=(X_size,self.hidden_layers))
        self._biases = np.random.normal(size=(self.hidden_layers))

    def _forward(self, X):
        G = np.dot(X, self._input_weights)
        G += self._biases
        H = self._relu(G)
        return H
    
    def train(self, X, y):
        # Init weights
        self._init_weights(X.shape[1])     
        mpinv = np.linalg.pinv(self._forward(X))
        self._output_weights = np.dot(mpinv, y)

    def predict(self, X):
        out = self._forward(X)
        preds = np.dot(out, self._output_weights)
        return preds

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

model = ELM(hidden_layers=5000)
model.train(x_train,y_train)
ac_count=0
wc_count=0
print("Predicted","\t\t","Accuracy")
print("............................")
for i,x in enumerate(x_test):
    pred = model.predict(x)
    acc = y_test[i]
    if (pred-acc<0.5):
      ac_count+=1
    else:
      wc_count=+1
    print(pred,"\t", acc)

accuracy=(ac_count-wc_count)/ac_count
print("Test Accuracy: {:.2f}%".format(accuracy * 100))

