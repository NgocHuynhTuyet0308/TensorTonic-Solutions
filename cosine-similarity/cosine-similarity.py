import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    
    # Tích vô hướng a.b 
    dot_product = np.dot(a, b)
    
    # Độ dài chuẩn của 2 vector
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if (norm_a == 0) or (norm_b == 0):
        return 0
    
    return dot_product / (norm_a * norm_b)