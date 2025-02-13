import numpy as np
def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    """ Argument 1: 2-by-3 array of triangle coordinates
    Argument 2: 1d array of point coordinates
    Returns: 1d array of barycentric coordinates"""
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]

    px, py= point_coordinates

    matrix = np.array([[x1, x2, x3],
                      [y1, y2, y3],
                      [1, 1, 1]])
    b = np.array([px, py, 1])
    barycentric_coordinates = np.linalg.solve(matrix, b)
    return barycentric_coordinates
  
def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    """ Argument 1: 2-by-3 array of triangle coordinates
    Argument 2: 1d array of point coordinates
    Returns: 1d array of cartesian coordinates"""
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]

    lambda1, lambda2, lambda3 = barycentric_coordinates

    px = lambda1 * x1 + lambda2 * x2 + lambda3 * x2
    py = lambda1 * y1 + lambda2 * y2 + lambda3 * y3

    return np.array([px, py])

def is_inside_triangle(triangle_coordinates, point_coordinates):
    """ Argument 1: 2-by-3 array of triangle coordinates
    Argument 2: 1d array of point coordinates
    Returns: 1d array of boolean indicating if point is inside triangle"""
    barycentric_coordinates = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return np.all(barycentric_coordinates >= 0)

triangle = np.array([[0, 5, 0],
                     [0, 0, 5],])

point = np.array([2,2])

barycentric_coordinates = get_barycentric_coordinates(triangle, point)
print(f'Barycentric coordinates: {barycentric_coordinates}')

cartesian_coordinates = get_cartesian_coordinates(triangle, barycentric_coordinates)
print(f'Cartesian coordinates: {cartesian_coordinates}')

inside_triangle = is_inside_triangle(triangle, point)
print(f'Inside triangle: {inside_triangle}')
