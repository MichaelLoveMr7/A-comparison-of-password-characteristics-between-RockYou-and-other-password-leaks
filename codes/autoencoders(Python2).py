#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:25:43 2020

@author: yujiedong
"""
# Simple TensorFlow LSTM Example
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

max_features = 1 # 0, 1, 2, 3
print(type(max_features))

'''
x=[
   [[0], [1], [1], [0], [0], [0]],
   [[0], [0], [0], [2], [2], [0]],
   [[0], [0], [0], [0], [3], [3]],
   [[0], [2], [2], [0], [0], [0]],
   [[0], [0], [3], [3], [0], [0]],
   [[0], [0], [0], [0], [1], [1]] 
]
'''
data = pd.read_csv("Matrix.csv")
x = data.iloc[:, 1]
y = data.iloc[:, 2]
x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size = 0.34,random_state = 42
        )
#print(type(x))
x_train = np.array(x_train, dtype = np.int32)
y_train = np.array(y_train,dtype=np.int32)
x_test = np.array(x_test, dtype = np.int32)
y_test = np.array(y_test,dtype=np.int32)
#print("x",x)
#print("type",type(x))
#print("y.shape[0]",y.shape[0])
#print("type(y.shape[0]",type(y.shape[0]))

# Convert y2 to dummy variables
#y2 = np.zeros((y.shape[0], max_features), dtype=np.float32)
#print("y2",y2)
#y2 = np.reshape(y2,(100,2))
#print("type(y2)",type(y2))
'''
print(y.shape[0])
print(y2[np.arange(y.shape[0]),y])
y2[np.arange(y.shape[0]),y] = 1.0
print("y2-2",y2)
print(y2.shape)
'''
#print("y2，1.0", y2)
#print("type(2)，1.0", type(y2))
#x = x.reshape(-1, 1)
#y = y.reshape(-1, 1)

print(x_train.shape[0])
#print(x_train.shape[2])
#How can I cange 2D array to 3D without value loss？
x_train = x_train.reshape(33, 2,1)
y_train = y_train.reshape(33, 2,1)
x_test = x_test.reshape(17, 2, 1)
y_test = y_test.reshape(17, 2, 1)

print("Build model...")
print(x_train.shape[1:])
model = Sequential()
#print(Sequential())
model.add(LSTM(128,  dropout=0.2, recurrent_dropout=0.2, input_shape=(x_train.shape[1:])))
#print(model)
model.add(Dense(2, activation = "sigmoid"))

# try using different optimizers and different optimizer configs
model.compile(loss = "binary_crossentropy",
              optimizer = "adam",
              metrics = ["accuracy"])
model.summary()
print("Train...")
model.fit(x_train, y_train, epochs = 200)
pred = model.predict(x_test)
predict_classes = np.argmax(pred, axis = 1)
print("Predicted classes: ()", predict_classes)
print("Expected classes: ()", predict_classes)


def runit(model, inp):
    inp = np.array(inp, dtype = np.float32)
    pred = model.predict(inp)
    return np.argmax(pred)

print("runit(model, [0])):",runit(model, [[0],[0],[0],
                                         [0],[0],[1]]))













