import numpy as np

def construct_matrix_C_k(k):
    if k == 1:
        # Base case for k=1
        return np.array([[1, -0.5], [-0.5, 1]])
    else:
        # Construct C_{k-1}
        C_k_minus_1 = construct_matrix_C_k(k - 1)
        size = 2 ** k
        
        # Create the matrix C_k with the appropriate size
        C_k = np.zeros((size, size))
        
        # Set the diagonal blocks to C_{k-1}
        C_k[:size//2, :size//2] = C_k_minus_1
        C_k[size//2:, size//2:] = C_k_minus_1
        
        # Fill the off-diagonal blocks
        off_diagonal_block = np.ones((size//2, size//2)) * (-2**-(2*k - 1))
        C_k[:size//2, size//2:] = off_diagonal_block
        C_k[size//2:, :size//2] = off_diagonal_block
        
        return C_k

