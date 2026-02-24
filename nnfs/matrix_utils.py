import numpy as np

def dot(a, b):
    dot_result = 0
    if len(a) != len(b):
        raise ValueError("Dot product is undefined for vectors of different lengths")
    else:
        dot_result = sum(np.multiply(a, b))
    return dot_result

def matmul(A, B):
    """
    Performs matrix multiplication between A and B.
    """
    return A @ B

def add_bias(X, b):
    """
    Adds bias vector b to each row of matrix X.
    """
    return X + b

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    a = [1, 2]
    b = [2, 1]
    print(dot(a, b))