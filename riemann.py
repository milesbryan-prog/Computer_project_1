import numpy as np

#Using Riemann sums to estimate the area under a curve by taking small, retangular or trapezoidal slices with the width defined by the differential
def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
# left_endpoint() uses the leftmost y value within the length of each slice.
#takes in a np array of x values and the function of the curve
#inputs all values from array into function and takes the difference on the
#array to find the width of each rectangle multiply and sum to get final answer
    values_on_curve = func(x_vals[0:-1])
    interval_size = np.subtract(x_vals[1::], x_vals[0:-1:])
    final = values_on_curve * interval_size
    final = np.sum(final)
    return final

def trapezoid(x_vals: np.ndarray, func: np.ufunc)->float:
# trapezoid() uses both the leftmost and rightmost y values to create trapezoidal
#calculates the base length of every value in the inputted array x_vals by running
# it through the inputted function func. Calculates height by subtracting the nearest
#intervals from one another. Preforms the trapizoid formula in two steps to confirm
#we do not have egregious parenthesis or minor arithmetic mistakes. Sums the final array
#with values and returns that array
    left_side_values = func(x_vals[0:-1])
    right_side_values = func(x_vals[1:])
    height_of_trap = np.subtract(x_vals[1:], x_vals[0:-1])
    top_of_fraction = (left_side_values+right_side_values) / 2
    final = top_of_fraction * height_of_trap
    final_sum = np.sum(final)
    return final_sum

    # height_of_interval = np.array([0])
    # size_of_array = len(x_vals)
    # height_of_interval = np.concatenate((height_of_interval, x_vals))
    # height_of_interval = np.subtract(x_vals, height_of_interval[:size_of_array])
    # left_base_of_trapezoid = func([x_vals[0::2]])
    # right_base_of_trapezoid = func([x_vals[1::2]])
    # top_of_fraction = np.add(left_base_of_trapezoid, right_base_of_trapezoid)
    # final_height_of_intervals = np.add(height_of_interval[0::2], height_of_interval[1::2])
    # final_trapizoid = ((top_of_fraction)/2) * final_height_of_intervals
    # final_trapizoid_summed_up = np.sum(final_trapizoid)
    # return final_trapizoid_summed_up

def simpson(x_vals: np.ndarray, func: np.ufunc)->float:
# simpson uses the midpoint of each slice for the height, defines the
# takes in a np array of x vals and a function for the curve
#finds the midpoint by adding together values next to each other and dividing by
#two plugs this into the function. Then calculates the width of interval by
#subtracting values next to one another to find distance between then function
#is performed on even and odd values in the array before the simspons formula is
#performed and summed giving us the final answer
    midpoint = np.add(x_vals[0:-1:], x_vals[1::]) / 2
    midpoint = func(midpoint)
    width  = np.subtract(x_vals[1::], x_vals[0:-1:])
    left_height = func(x_vals[0:-1:])
    right_height = func(x_vals[1::])
    simpson_sum = (width/6) * (left_height + (4 * (midpoint)) + right_height)
    simpson_sum = np.sum(simpson_sum)
    return simpson_sum
