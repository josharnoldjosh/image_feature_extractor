# Image Feature Extractor 

## What is it?

Python scripts to extract image features from images within a directory, and then cluster the MOST similar images into different sets. Very easy to use and customize!

## Requirements

* Requires hickle
* Should use python2 (python3 may not work)

## Usage 

* Navigate to a directory that contains images
* Run `group_images.py` in that directory. It will recurse folders and create an `images` folder with all images copied and renamed in that directory
* Run `extract.py` to extract image features
* Run `create_matrix.py` 
* Run `create_matrix_T.py` 
* Run `dot.py` 
* Run `compile_similar.py` to finally output your desired images 

Edit `compile_similar.py` to adjust how many images are grouped together and how many sets of images to cluster.
