# importing dependencies
#read kaggle facial expression recognition challenge dataset (fer2013.csv)
#https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Conv2D,MaxPooling2D,BatchNormalization
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam, SGD
from keras.optimizers import   RMSprop
from keras.regularizers import l2
from keras.utils import np_utils

# Loading dataset
df=pd.read_csv('data/fer2013/fer2013.csv')
print(df.info())
# print(df["Usage"].value_counts())
# print(df["Usage"].value_counts)
print(df.head())

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

print(f"X_train sample data:{X_train[0:2]}")
print(f"Y_train sample data:{Y_train[0:2]}")
print(f"X_test sample data:{X_test[0:2]}")
print(f"Y_test sample data:{Y_test[0:2]}")

X_train=np.array(X_train,'float32')
Y_train=np.array(Y_train,'float32')
X_test=np.array(X_test,'float32')
Y_test=np.array(Y_test,'float32')

num_features=64
num_labels=7
batch_size=256
epochs=30
width,height=48,48

Y_train=np_utils.to_categorical(Y_train , num_classes=num_labels)
Y_test=np_utils.to_categorical(Y_test, num_classes=num_labels)

# Normalizing

X_train/=255
X_test/=255


X_train=X_train.reshape(X_train.shape[0],width,height,1)
X_train=X_train.astype('float32')
X_test=X_test.reshape(X_test.shape[0],width,height,1)
X_test=X_test.astype('float32')

# design in CNN

model=Sequential()

#1st convolution layer
model.add(Conv2D(64, kernel_size=(5, 5), activation='relu', input_shape=(48,48,1)))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(5,5), strides=(2, 2)))

#2nd convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
#model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(3,3), strides=(2, 2)))

#3rd convolution layer
model.add(Conv2D(128, (3, 3), activation='relu'))
#model.add(Conv2D(128, (3, 3), activation='relu'))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(3,3), strides=(2, 2)))

model.add(Flatten())

#fully connected neural networks
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_labels, activation='softmax'))

# model.summary()
#Compliling the model
model.compile(loss=categorical_crossentropy,
              optimizer=RMSprop(),
              metrics=['accuracy'])

#Training the model
model.fit(X_train, Y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(X_test, Y_test),
          shuffle=True)


#Saving the  model to  use it later on
fer_json = model.to_json()
with open("fer.json", "w") as json_file:
    json_file.write(fer_json)
model.save_weights("fer.h5")