import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    x_values_shifted = np.array([0])
    size = len(x_vals)
    #np.append(x_vals, 6)
    x_values_shifted = np.concatenate((x_values_shifted, x_vals))
    x_vals_function = func(x_vals[:size - 1])
    x_values_shifted = x_values_shifted[0: size]
    multiply_by = np.subtract(x_vals, x_values_shifted)
    size_final = len(multiply_by)
    multiply_by =  multiply_by[:size_final - 1]
    final = multiply_by * x_vals_function
    final = sum(final)
    return final


def trapezoid(x_vals: np.ndarray, func: np.ufunc)->float:
    height = np.array([0])
    size = len(x_vals)
    height = np.concatenate((height, x_vals))
    height = x_vals - height[:size]
    left_base = func([x_vals[0::2]])
    right_base = func([x_vals[1::2]])
    top_of_fraction = np.add(left_base, right_base)
    height = height[0::2] + height[1::2]
    final_trap = ((top_of_fraction)/2) * height
    final_trap = np.sum(final_trap)
    return final_trap


def simpson(x_vals: np.ndarray, func: np.ufunc)->float:
    midpoint = np.add(x_vals[0::2], x_vals[1::2]) / 2
    midpoint = func(midpoint)
    width = np.subtract(x_vals[1::2], x_vals[0::2])
    left_height = func(x_vals[0::2])
    right_height = func(x_vals[1::2])
    simpson_sum = (width/6) * (left_height + (4 * (midpoint)) + right_height)
    simpson_sum = np.sum(simpson_sum)
    return simpson_sum
