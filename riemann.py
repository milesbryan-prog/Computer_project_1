import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    size = len(x_vals)
    x_vals = x_vals[:size - 1]
