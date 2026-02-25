import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    return A.transpose(1, 0)
