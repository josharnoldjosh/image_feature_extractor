from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import os
from glob import glob
import numpy as np
import pickle
from PIL import Image
import h5py

def LoadImages():
	print("Loading image files...")
	image_list = []
	for filename in glob('images/*.jpg'):
	    print(filename)
	    image_list.append(filename)
	return image_list

def ExtractImageFeature(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    vgg16_feature = model.predict(img_data)
    return np.array(vgg16_feature).flatten()

extracted_image_features = []

model = VGG16(weights='imagenet', include_top=False)

i = 0
images = LoadImages()
for path in images:
	i += 1
	feature = ExtractImageFeature(path)
	data = (path, feature)
	extracted_image_features.append(data)
	print(i, "out of", len(images))
	if (i == 100):
		break

import hickle
hickle.dump(extracted_image_features, 'output.hkl', mode='w', compression='gzip')

print("Script done!")
