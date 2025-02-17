import numpy as np

#Using Riemann sums to estimate the area under a curve by taking small, retangular or trapezoidal slices with the width defined by the differential
def left_endpoint(x_vals: np.ndarray, func: np.ufunc)->float:
# left_endpoint() uses the leftmost y value within the length of each slice.
#width of rectangle represents the value between consecutive terms also know as
# the height of the rectangle when calculating riemann sums. Values on curve is the
#array values plugged into the given function. Multiply by is an array with all the
#final values of rectnagle heights with the final one taken off to account for this
#being a left hand sum. final is the result of the multipation and summed for final answer
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
# trapezoid() uses both the leftmost and rightmost y values to create trapezoidal
# slices. height of interval represents the height in the traizoidal area equation is
# the value of the values next to each other susbtracted from one another to calculate
# the distance "height" of the sum, left and right bases are slices that are plugged
#into the function then used to pre calculate the top of fraction to avoid divsion
#errors, final height is adding the two function slices together to get the final value
# trapizoid formula is performed then summed
    height_of_interval = np.array([0])
    size_of_array = len(x_vals)
    height_of_interval = np.concatenate((height_of_interval, x_vals))
    height_of_interval = np.subtract(x_vals, height_of_interval[:size_of_array])
    left_base_of_trapezoid = func([x_vals[0::2]])
    right_base_of_trapezoid = func([x_vals[1::2]])
    top_of_fraction = np.add(left_base_of_trapezoid, right_base_of_trapezoid)
    final_height_of_intervals = np.add(height_of_interval[0::2], height_of_interval[1::2])
    final_trapizoid = ((top_of_fraction)/2) * final_height_of_intervals
    final_trapizoid_summed_up = np.sum(final_trapizoid)
    return final_trapizoid_summed_up

def simpson(x_vals: np.ndarray, func: np.ufunc)->float:
# simpson uses the midpoint of each slice for the height, defines the
# midpoint by adding the values in the function and dividing them by 2 to find
# the average or "middle" value then plugs these values into the given funciton.
#calculates width by subtracting elements next to each other in inputted array
#calculates left and right value of function by taking a slice of the orginal
#function and plugging these values into the function. Then the simpson forumula
#is performed
    size = len(x_vals)
    midpoint = np.add(x_vals[0::-1], x_vals[1::]) / 2
    midpoint = func(midpoint)
    width  = np.subtract(x_vals[1::], x_vals[0:size-1:])
    left_height = func(x_vals[0::-1])
    right_height = func(x_vals[1::])
    simpson_sum = (width/6) * (left_height + (4 * (midpoint)) + right_height)
    simpson_sum = np.sum(simpson_sum)
    return simpson_sum
