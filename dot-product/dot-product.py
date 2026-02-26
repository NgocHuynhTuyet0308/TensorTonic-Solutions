import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    
    if norm_x == 0 or norm_y == 0:
        return 0.0
    
    dot_product = np.dot(x, y)
    
    cos_theta = dot_product / (norm_x * norm_y)
    
    return float(norm_x * norm_y * cos_theta)