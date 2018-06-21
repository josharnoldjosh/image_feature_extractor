import hickle
import numpy as np

# Load file
print("Loading file!")
file = hickle.load('output.hkl')

# Create matrix
print("Creating matrix...")
matrix = np.empty(shape=(len(file), len(file[0][1])))
for i in range(0, len(file)):	
	matrix[i] = file[i][1]

print("Saving matrix...")
hickle.dump(matrix.T, 'matrix_T.hkl', mode='w', compression='gzip')

print("Script done :)")

# print("Doing the dot... (with integers)")
# S = np.dot(matrix, matrix.T)



