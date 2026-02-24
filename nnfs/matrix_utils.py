import numpy as np
def dot(a, b):
    """
    Computes dot product between two vectors.
    """
    return np.dot(a, b)

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
    print(matmul(A, B))