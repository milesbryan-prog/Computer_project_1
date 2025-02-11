import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    x_values_shifted = np.array([0])
    size = len(x_vals)
    np.append(x_vals, 6)
    x_values_shifted = np.stack(x_values_shifted, x_vals)
    x_vals_function = func(x_vals[:size - 1])
    x_values_shifted = x_values_shifted[0: size - 1]
    x_vals.reshape(1,1)
    x_values_shifted.reshape(1,1)
    multiply_by = np.subtract(x_vals - x_values_shifted)
    final = multiply_by * x_vals_function
    final = sum(final)
    return final
