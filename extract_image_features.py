#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:18:58 2018

@author: josharnold
"""

from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import os
from glob import glob
import numpy as np
import pickle

print("Loading stuff...")

def GetImagePaths(pattern="*.jpg"):
    files = []
    for dir,_,_ in os.walk(os.getcwd()):
        files.extend(glob(os.path.join(dir,pattern)))
    return files

# Create model
model = VGG16(weights='imagenet', include_top=False)

def ExtractImageFeature(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    vgg16_feature = model.predict(img_data)
    return np.array(vgg16_feature).flatten()

image_paths = GetImagePaths()

extracted_image_features = []

i = 1
for path in image_paths:
    feature = ExtractImageFeature(path)
    data = (path, feature)
    extracted_image_features.append(data)
    print(i, "out of", len(image_paths))
    i += 1
    
with open('extracted_image_features.pkl', 'wb') as f:
    pickle.dump(extracted_image_features, f)
    
print("Script done :)")