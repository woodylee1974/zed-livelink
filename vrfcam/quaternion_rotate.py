import numpy as np


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

    # Apply the rotation quaternion to v1 to get the rotated v1
    rotated_v1 = quaternion_rotate(q, v1)

    return rotated_v1


def quaternion_rotate(q, v):
    # Convert quaternion to rotation matrix
    q_conj = np.array([q[0], -q[1], -q[2], -q[3]])
    rotation_matrix = quaternion_to_rotation_matrix(q)

    # Apply rotation matrix to vector
    rotated_v = np.dot(rotation_matrix, v)

    return rotated_v


def quaternion_to_rotation_matrix(q):
    w, x, y, z = q
    rotation_matrix = np.array([
        [1 - 2 * y ** 2 - 2 * z ** 2, 2 * x * y - 2 * w * z, 2 * x * z + 2 * w * y],
        [2 * x * y + 2 * w * z, 1 - 2 * x ** 2 - 2 * z ** 2, 2 * y * z - 2 * w * x],
        [2 * x * z - 2 * w * y, 2 * y * z + 2 * w * x, 1 - 2 * x ** 2 - 2 * y ** 2]
    ])

    return rotation_matrix

v0 = [1, 0, 0]
v1 = [0, 1, 0]

rotated_v0 = quaternion_from_two_vectors(v1, v0)
print("Rotated v0:", rotated_v0)

rotated_v1 = quaternion_from_two_vectors(v0, v1)
print("Rotated v1:", rotated_v1)

