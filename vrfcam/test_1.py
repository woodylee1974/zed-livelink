import numpy as np
import math


def quaternion_from_two_vectors(v0, v1):

    v0 = np.asarray(v0)
    v1 = np.asarray(v1)
    v0 = v0 / np.linalg.norm(v0)  # Normalize vectors
    v1 = v1 / np.linalg.norm(v1)

    cos_theta = np.dot(v0, v1)
    if cos_theta < -1 + 1e-6:
        v1 = np.cross([1, 0, 0], v0)
        if np.linalg.norm(v1) < 1e-6:
            v1 = np.cross([0, 1, 0], v0)
        v1 = v1 / np.linalg.norm(v1)
        q = np.array([0.0, v0[2], -v0[1], v0[0]])
    else:
        axis = np.cross(v0, v1)
        s = np.sqrt((1 + cos_theta) * 2)
        q = np.array([s / 2.0, axis[0] / s, axis[1] / s, axis[2] / s])
    return q


def quaternion_to_euler(q):

    w, x, y, z = q
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t3, t4)

    return roll_x, pitch_y, yaw_z


def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

    return np.array([w, x, y, z])


# Example usage:
v0 = np.array([1.0, 0.0, 0.0])
v1 = np.array([0.0, 1.0, 0.0])
v2 = np.array([0.0, 0.0, 1.0])
rotation_quaternion1 = quaternion_from_two_vectors(v0, v1)
rotation_quaternion2 = quaternion_from_two_vectors(v1, v2)

q_total = quaternion_multiply(rotation_quaternion1, rotation_quaternion2)
print("Rotation quaternion1:", rotation_quaternion1)
print("Rotation quaternion2:", rotation_quaternion2)

euler_angles1 = quaternion_to_euler(rotation_quaternion1)
print("Euler angles1:", np.degrees(euler_angles1))
euler_angles2 = quaternion_to_euler(rotation_quaternion2)
print("Euler angles2:", np.degrees(euler_angles2))
euler_angles_t = quaternion_to_euler(q_total)
print("Euler angles_t:", np.degrees(euler_angles_t))
