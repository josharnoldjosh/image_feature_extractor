import hickle
import numpy as np
from PIL import Image
import os, shutil
from shutil import copyfile

file = hickle.load('output.hkl')

# Create matrix
vector_array = []
for i in file:
	vector_array.append(i[1])
matrix = np.array(vector_array)
matrix_T = matrix.T
S = np.dot(matrix, matrix_T)

# Get indexes of max
def GetSimilarIndices(row, num_similar_images):
	sorted_row = row.tolist()
	sorted_row = sorted(sorted_row, key=int, reverse=True)
	sorted_row = sorted_row[1:num_similar_images+1]
	indices = []
	for i in sorted_row:
		indices.append(row.tolist().index(i))
	return indices

image_sets = []
for row in S:
	indices = GetSimilarIndices(row, 20)
	similar_images = []
	for i in indices:
		similar_images.append(file[i][0])
	image_sets.append(similar_images)

if os.path.exists("output"):
	shutil.rmtree("output")

for image_set in image_sets:
	output = os.path.join("output",str(image_sets.index(image_set)+1))	
	os.makedirs(output)
	for image in image_set:
		dest = output + "/" + str(image_set.index(image)+1) + ".jpg"		
		copyfile(image, dest)

print("Script done :)")

