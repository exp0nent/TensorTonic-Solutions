import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x_np = np.asarray(x, dtype=float)
    result = 1 / (1 + np.exp(-x_np))
    
    # Return type handling
    if np.isscalar(x):
        return float(result)
    return result.tolist()
