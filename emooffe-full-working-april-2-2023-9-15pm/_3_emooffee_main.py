'''
Title : Main run file for Emooffee
Date Created : March 20, 2023 | Last Updated : April 2, 2023
Python version 3.9.16 
'''


# ----- Imports
import numpy as np
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
from keras.applications.mobilenet import MobileNet 
import matplotlib.pyplot as plt
from keras.models import Model
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Flatten, Dense


# ----- Working
def emooffee_analyse(img_path):
    base_model = MobileNet(input_shape=(224,224,3), include_top= False)

    for layer in base_model.layers:
        layer.trainable = False

    x = Flatten()(base_model.output)
    x = Dense(units=7 , activation='softmax' )(x)

    model = Model(base_model.input, x)

    train_datagen = ImageDataGenerator(
        zoom_range = 0.2, 
        shear_range = 0.2, 
        horizontal_flip=True, 
        rescale = 1./255
    )

    train_data = train_datagen.flow_from_directory(directory = 'python/emooffee/dataset/train', 
                                                                            target_size=(224,224),
                                                                            batch_size=32
                                                                            )

    model = load_model("best_model.h5")
    # path for the image to see if it predics correct class
    # example of loading an image with the Keras API

    # User image run
    path = img_path
    
    img = load_img(path, target_size=(224,224))

    i = img_to_array(img)/255
    input_arr = np.array([i])

    pred = np.argmax(model.predict(input_arr))

    # just to map o/p values 
    op = dict(zip( train_data.class_indices.values(), train_data.class_indices.keys()))

    return str.upper(op[pred])
