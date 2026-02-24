import numpy as np

def dot(a, b):
    dot_result = 0
    if len(a) != len(b):
        raise ValueError("Dot product is undefined for vectors of different lengths")
    else:
        print(np.multiply(a, b))
        dot_result = sum(np.multiply(a, b))
        print(dot_result)
    return dot_result

def matmul(A, B):
    matrixA_dim = [len(A), len(A[0])]
    matrixB_dim = [len(B), len(B[0])]
    multimatrx = np.empty((matrixA_dim[0], matrixB_dim[1]))
    print(multimatrx)
    if matrixA_dim[1] != matrixB_dim[0]:
        raise ValueError("Matrices cannot be multiplied")
    else:
        B_t = B.transpose()
        for i in range(matrixA_dim[0]):
            print("i =", i)
            for j in range(matrixB_dim[1]):
                print("j =", j)
                element = dot(A[i], B_t[j])
                print(element)
                multimatrx[i][j] = element
    return multimatrx

def add_bias(X, b):
    """
    Adds bias vector b to each row of matrix X.
    """
    return X + b

if __name__ == "__main__":
    A = np.array([[1, 2, 5, 7], [6, 4, 2, 9], [5, 6, 0, -1]])
    B = np.array([[2, 5], [4, -3], [0, 1], [-2, 4]])
    print(matmul(A, B))