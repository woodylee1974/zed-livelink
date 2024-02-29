
def interpolate_point(pt1, pt2, t):
    """
    Interpolate a point between two given points.

    pt1: First point (x, y, z)
    pt2: Second point (x, y, z)
    t: Interpolation factor (0 <= t <= 1)
    """
    mid_x = pt1[0] + (pt2[0] - pt1[0]) * t
    mid_y = pt1[1] + (pt2[1] - pt1[1]) * t
    mid_z = pt1[2] + (pt2[2] - pt1[2]) * t
    return mid_x, mid_y, mid_z


def midpoint(pt1, pt2, a, b):
    mid_x = (a * pt1[0] + (b - a) * pt2[0]) / b
    mid_y = (a * pt1[1] + (b - a) * pt2[1]) / b
    mid_z = (a * pt1[2] + (b - a) * pt2[2]) / b
    new_point = (mid_x, mid_y, mid_z)
    return new_point

# Example usage:
pt2 = (1, 2, 3)
pt1 = (4, 5, 6)
# t = -1  # Interpolation factor
# mid_point = interpolate_point(pt1, pt2, t)
# print(mid_point)  # Output: (2.5, 3.5, 4.5)

a, b = 3, 4
mid_point = midpoint(pt1, pt2, a, b)
print(mid_point)  # Output: (2.5, 3.5, 4.5)