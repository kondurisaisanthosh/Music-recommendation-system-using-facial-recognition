import os
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D,MaxPooling2D,BatchNormalization
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.utils import np_utils

df=pd.read_csv('data/fer2013/fer2013.csv')
# print(df.info())
# print(df["Usage"].value_counts())
# print(df["Usage"].value_counts)
# print(df.head())

X_train,Y_train,X_test,Y_test=[],[],[],[]

for index,row in df.iterrows():
    val=row['pixels'].split(" ")
    try:
        if 'Training' in row['Usage']:
            X_train.append(np.array(val,'float32'))
            Y_train.append(row['emotion'])
        elif 'PublicTest' in row['Usage']:
            X_test.append(np.array(val, 'float32'))
            Y_test.append(row['emotion'])
    except:
        print(f"Error occured at index:{index} and row:{row}")