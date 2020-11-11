from keras import layers
from keras import models
from keras.preprocessing import image
import os,shutil
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras import optimizers
from keras import regularizers
from sklearn.metrics import classification_report,confusion_matrix
from keras.models import load_model
import pandas as pd
    
    #Generatory zwracające wszystkie pliki z danego foldera i jego podfolderów
    #Podfolder jest traktowany jako odzielna etykeita
    #Przeskalowane z 3 wymiarów (RGB) do 1 wymiaru 
    train_datagen = ImageDataGenerator(
        rescale=1./255
    )
    validation_datagen = ImageDataGenerator(rescale=1./255)

    print(train_generator.class_indices.items())

    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,target_size=(20,32),batch_size=90,class_mode='categorical'
    )


    #Architektura sieci
    model = models.Sequential()
    model.add(layers.Conv2D(256,(3,3),activation='relu',input_shape=(20,32,3)))
    model.add(layers.MaxPool2D((2,2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256,activation='relu'))
    model.add(layers.Dense(1024,activation='relu'))
    model.add(layers.Dense(89,activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['acc'])

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=1900,
        epochs=6,
        validation_data=validation_generator,
        validation_steps=504,
        use_multiprocessing=False
    )



    model.save("256__256_1024_6.h5")
