from capture import Capture as cp

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os


def Model():
    
    # This is the input size which our model accepts.
    image_size = 224
    
    # Loading pre-trained NASNETMobile Model without the head by doing include_top = False
    N_mobile = tf.keras.applications.NASNetMobile( input_shape=(image_size, image_size, 3), include_top=False, weights='imagenet')
    
    # Freeze the whole model 
    N_mobile.trainable = False
        
    # Adding our own custom head
    # Start by taking the output feature maps from NASNETMobile
    x = N_mobile.output
    
    # Convert to a single-dimensional vector by Global Average Pooling. 
    # We could also use Flatten()(x) GAP is more effective reduces params and controls overfitting.
    x = GlobalAveragePooling2D()(x)
    
    # Adding a dense layer with 712 units
    x = Dense(712, activation='relu')(x) 
    
    # Dropout 40% of the activations, helps reduces overfitting
    x = Dropout(0.40)(x)
    
    # The fianl layer will contain 4 output units (no of units = no of classes) with softmax function.
    preds = Dense(4,activation='softmax')(x) 
    
    # Construct the full model
    model = Model(inputs=N_mobile.input, outputs=preds)
    
    # Check the number of layers in the final Model
    print ("Number of Layers in Model: {}".format(len(model.layers[:])))
    

if __name__ == "__main__":

    cp.Collect(10)
    cp.Show()
