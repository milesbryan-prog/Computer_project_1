import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
    width_of_rectangle_in_sum = np.array([0])
    size = len(x_vals)
    width_of_rectangle_in_sum = np.concatenate((width_of_rectangle_in_sum, x_vals))
    values_on_the_curve = func(x_vals[:size - 1])
    width_of_rectangle_in_sum = width_of_rectangle_in_sum[0: size]
    multiply_by = x_vals - width_of_rectangle_in_sum
    size_final = len(multiply_by)
    multiply_by =  multiply_by[:size_final - 1]
    final = multiply_by * values_on_the_curve
    final = sum(final)
    return final


def trapezoid(x_vals: np.ndarray, func: np.ufunc)->float:
    height_of_interval = np.array([0])
    size_of_array = len(x_vals)
    height_of_interval = np.concatenate((height_of_interval, x_vals))
    height_of_interval = x_vals - height_of_interval[:size_of_array]
    left_base_of_trapezoid = func([x_vals[0::2]])
    right_base_of_trapezoid = func([x_vals[1::2]])
    top_of_fraction = left_base_of_trapezoid + right_base_of_trapezoid
    final_height_of_intervals = height_of_interval[0::2] + height_of_interval[1::2]
    final_trapizoid = ((top_of_fraction)/2) * final_height_of_intervals
    final_trapizoid_summed_up = np.sum(final_trapizoid)
    return final_trapizoid_summed_up


def simpson(x_vals: np.ndarray, func: np.ufunc)->float:
    midpoint = np.add(x_vals[0::2], x_vals[1::2]) / 2
    midpoint = func(midpoint)
    width  = x_vals[1::2] - x_vals[0::2]
    left_height = func(x_vals[0::2])
    right_height = func(x_vals[1::2])
    simpson_sum = (width/6) * (left_height + (4 * (midpoint)) + right_height)
    simpson_sum = np.sum(simpson_sum) * 2
    return simpson_sum
