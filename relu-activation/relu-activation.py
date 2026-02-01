import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)

    # Handle scalar input
    if x.ndim == 0:
        x = x.reshape(1,)

    return np.maximum(0, x)