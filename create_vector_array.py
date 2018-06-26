import hickle
import numpy

# Load file
print("Loading file!")
file = hickle.load('output.hkl')

# Create matrix
print("Creating matrix...")
vector_array = []
for i in file:
	vector_array.append(i[1].tolist())

print("Saving array...")
hickle.dump(vector_array, 'vector_array.hkl', mode='w', compression='gzip')

print("Script done :)")