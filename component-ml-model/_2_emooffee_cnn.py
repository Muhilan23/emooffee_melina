'''
Title : CNN Algorithm file for Emooffee
Date Created : March 20, 2023 | Last Updated : April 2, 2023
Python version 3.9.16 
'''


#-----Imports
import matplotlib.pyplot as plt
from PIL import *
from keras.layers import Flatten, Dense
from keras.models import Model
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import MobileNet 
from keras.losses import categorical_crossentropy
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import load_model


#-----Working with pre trained model 
base_model = MobileNet(input_shape=(224,224,3), include_top= False )

for layer in base_model.layers:
    layer.trainable = False

x = Flatten()(base_model.output)
x = Dense(units=7 , activation='softmax' )(x)

# creating our model.
model = Model(base_model.input, x)

model.compile(optimizer='adam', loss= categorical_crossentropy, 
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    zoom_range = 0.2, 
    shear_range = 0.2, 
    horizontal_flip=True, 
    rescale = 1./255
)

train_data = train_datagen.flow_from_directory(directory = 'python/emooffee/dataset/train', 
                                               target_size=(224,224),
                                               batch_size=32,)



val_datagen = ImageDataGenerator(rescale = 1./255 )

val_data = val_datagen.flow_from_directory(directory= "python/emooffee/dataset/test", 
    target_size=(224,224), 
    batch_size=32,
    )

## having early stopping and model check point 
# early stopping
es = EarlyStopping(monitor='val_accuracy', 
                   min_delta= 0.01 , 
                   patience= 5, 
                   verbose= 1, 
                   mode='auto')

# model check point
mc = ModelCheckpoint(filepath="best_model.h5", 
    monitor= 'val_accuracy', 
    verbose= 1, 
    save_best_only= True, 
    mode = 'auto'
    )

# puting call back in a list 
call_back = [mc]

hist = model.fit_generator(train_data, 
    steps_per_epoch= 10, 
    epochs= 100, 
    validation_data= val_data, 
    validation_steps= 8, 
    callbacks=[mc]
    )

model = load_model("best_model.h5")
h =  hist.history
h.keys()

plt.plot(h['accuracy'])
plt.plot(h['val_accuracy'] , c = "red")
plt.title("acc vs v-acc")
plt.show()

plt.plot(h['loss'])
plt.plot(h['val_loss'] , c = "red")
plt.title("loss vs v-loss")
plt.show()

# just to map o/p values 
op = dict(zip( train_data.class_indices.values(), train_data.class_indices.keys()))