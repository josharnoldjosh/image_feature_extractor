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
matrix = np.array(vector_array).astype(int) # int is faster

print(matrix)

print("Doing the dot... (with integers)")
S = np.dot(matrix, matrix.T)
print("Dot done! Saving matrix...")

hickle.dump(S, 'matrix.hkl', mode='w', compression='gzip')

print("Script done :)")

#Test


