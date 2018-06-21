import hickle
import numpy as np

print("Loading matrix!")
matrix = hickle.load('matrix.hkl')

print("Loading matrix.T!")
matrix_T = hickle.load('matrix_T.hkl')

print("Doing the dot!")
S = np.dot(matrix, matrix_T)

print("Saving matrix S!")
hickle.dump(S, 'matrix_S.hkl', mode='w', compression='gzip')

print("Script done :)")