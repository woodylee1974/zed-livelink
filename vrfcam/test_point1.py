import numpy as np


def perpendicular_bisector(a, b, k):
    mid_point = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    direction_vector = np.array([b[1] - a[1], -(b[0] - a[0])])  # Perpendicular vector
    direction_vector = - direction_vector
    unit_direction_vector = direction_vector / np.linalg.norm(direction_vector)
    c = mid_point + k * unit_direction_vector
    x, y = c[0], c[1]
    c = (x, y)
    return c

# 示例使用：
point_a = (2, 0)
point_b = (-2, 0)
distance_k = 3

point_c = perpendicular_bisector(point_a, point_b, distance_k)
print("Point C:", point_c)
