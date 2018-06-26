# Image Feature Extractor 

## What is it?

Python scripts to extract image features from images within a directory, and then cluster the MOST similar images into different sets. Very easy to use and customize!

## Requirements

* Requires hickle
* Should use python2 (python3 may not work)

## Usage 

### Clustering via matrices (recommended)

* Navigate to a directory that contains images
* Run `group_images.py` in that directory. It will recurse folders and create an `images` folder with all images copied and renamed in that directory
* Run `extract.py` to extract image features
* Run `create_matrix.py` 
* Run `create_matrix_T.py` 
* Run `dot.py` 
* Run `compile_similar.py` to finally output your desired images 

Edit `compile_similar.py` to adjust how many images are grouped together and how many sets of images to cluster.

### Clustering via k means (good if matrices give memory error)
* Navigate to a directory that contains images
* Run `group_images.py` in that directory. It will recurse folders and create an `images` folder with all images copied and renamed in that directory
* Run `cluster.py [number of image sets] [number of clusters] [iterations]`

An example of running `cluster.py` is:

`cluster.py 10 20 100`

This would generate 10 folders each with a number of images inside of them. It would cluster your data into 20 clusters and iterate over them 100 times. The more iterations, the less images you will have per folder. the less iterations, the more images you will have per folder. 

