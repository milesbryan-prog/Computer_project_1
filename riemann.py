
import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    x_values_shifted = np.array([0])
    size = len(x_vals)
    #np.append(x_vals, 6)
    x_values_shifted = np.concatenate((x_values_shifted, x_vals))
    x_vals_function = func(x_vals[:size - 1])
    x_values_shifted = x_values_shifted[0: size]
    x_vals.reshape(1,size)
    x_values_shifted.reshape(1,size)

    multiply_by = np.subtract(x_vals, x_values_shifted)
    size_final = len(multiply_by)
    multiply_by =  multiply_by[:size_final - 1]
    final = multiply_by * x_vals_function
    final = sum(final)
    return final


def trapezoid(x_vals: np.ndarray, func: np.ufunc)->float:
    size = len(x_vals)
    height = np.array([0])
    size = len(x_vals)
    # np.append(x_vals, 6)
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
    size = len(x_vals)
    range = (x_vals[size - 1] - x_vals[0])
    mid_point = ((x_vals[0] + x_vals[size-1])/2)
    final_simp = (range/6) * (func(x_vals[0]) + 4*func(mid_point) + func(x_vals[size-1]))
    float(final_simp)
    return final_simp
