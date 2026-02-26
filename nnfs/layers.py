import numpy as np
from .matrix_utils import matmul, add_bias


class Linear:
    def __init__(self, input_dim, output_dim):
        # Initialize weights small random numbers
        self.W = np.random.randn(input_dim, output_dim) * 0.01
        self.b = np.zeros((1, output_dim))

    def forward(self, X):
        return add_bias(matmul(X, self.W), self.b)
    
if __name__ == "__main__":
    X = np.random.randn(5, 3)  # 5 samples, 3 features
    layer = Linear(3, 2)
    output = layer.forward(X)
    print(output.shape)