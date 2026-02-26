import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    Tính tổng các giá trị trên đường chéo chính
    """
    A = np.array(A)
    return np.trace(A)
