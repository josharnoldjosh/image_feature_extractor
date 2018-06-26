import hickle
import numpy as np
from PIL import Image
import os, shutil
from shutil import copyfile

print("Loading file...")
file = hickle.load('output.hkl')
print("File loaded")

print("Loading matrix...")
S = hickle.load('matrix_S.hkl')
print("Matrix loaded")

# Get indexes of max
def GetSimilarIndices(row, num_similar_images):
	sorted_row = row.tolist()
	sorted_row = sorted(sorted_row, key=int, reverse=True)
	sorted_row = sorted_row[1:num_similar_images+1]
	indices = []
	for i in sorted_row:
		indices.append(row.tolist().index(i))
	return indices

print("Compiling")
if os.path.exists("output"):
	shutil.rmtree("output")

# Parameters
num_similar_images = 20
N_image_sets = 50

# Find highest similar image sets
row_sums = []
for row in S:
	num = sum(row)
	row_sums.append(num)	
sorted_row_sums = row_sums
sorted_row_sums = sorted(sorted_row_sums, key=int, reverse=True)
sorted_row_sums = sorted_row_sums[:N_image_sets]
row_indices = []
for i in sorted_row_sums:
	row_indices.append(row_sums.index(i))

image_sets = []
for i in range(0, N_image_sets):
	row = S[row_indices[i]]
	indices = GetSimilarIndices(row, num_similar_images)
	similar_images = []
	for i in indices:
		similar_images.append(file[i][0])
	image_sets.append(similar_images)

for image_set in image_sets:
	output = os.path.join("output",str(image_sets.index(image_set)+1))	
	os.makedirs(output)
	for image in image_set:
		dest = output + "/" + str(image_set.index(image)+1) + ".jpg"		
		copyfile(image, dest)

print("Done!")