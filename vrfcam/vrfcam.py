import socket
import struct
import numpy as np
import math


def points_to_orientation(pt1, pt2):
    # Base point
    y1, z1, x1 = pt1
    y2, z2, x2 = pt2
    
    # Vector representing the direction of the line segment
    direction = np.array([x2 - x1, y2 - y1, z2 - z1])
    direction = direction / np.linalg.norm(direction)  # Normalize

    # Default reference vector (along the x-axis)
    reference = np.array([0.0, 0.0, -1.0])
    reference = reference / np.linalg.norm(reference)

    # Calculate quaternion
    axis = np.cross(reference, direction)
    angle = math.acos(np.dot(reference, direction))
    s = math.sin(angle / 2)
    x, y, z = axis * s
    w = math.cos(angle / 2)

    # Normalize quaternion
    norm = math.sqrt(x ** 2 + y ** 2 + z ** 2 + w ** 2)
    orientation = (x / norm, y / norm, z / norm, w / norm)

    return pt1, orientation


def normalize_vector(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


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


class Bone:
    def __init__(self):
        self.translate = (0.0, 0.0, 0.0)
        self.orientation = (0.0, 0.0, 0.0, 0.0)


class SkeletonData:

    def __init__(self, name):
        self.name = name
        self.bones = []

    def add_bone(self, bone):
        self.bones.append(bone)


def create_skeleton_data(role_name, segments):
    # p0, p1 = segments[0]
    # x0, z0, y0 = p0
    # x1, z1, y1 = p1
    # delta = np.array([x1, y1, z1]) - np.array([x0, y0, z0])
    # delta = np.array(p1) - np.array(p0)
    # print(delta)
    data = SkeletonData(role_name)
    for pt1, pt2 in segments:
        bone = Bone()
        bone.translate, bone.orientation = points_to_orientation(pt1, pt2)
        data.bones.append(bone)
    return data


# def create_skeleton_data1(role_name, segments1, p, x, y, z, w):
#     data = SkeletonData(role_name)
#     for pt1, pt2 in segments1:
#         bone = Bone()
#         bone.translate, bone.orientation = p, (x, y, z, w)
#         data.bones.append(bone)
#     return data

def create_skeleton_data1(role_name, segments1, translations, orientations):
    data = SkeletonData(role_name)
    for (pt1, pt2), p, (w, x, y, z) in zip(segments1, translations, orientations):
        bone = Bone()
        bone.translate, bone.orientation = p, (x, y, z, w)
        data.bones.append(bone)
    return data


class TCPDataSender:
    def __init__(self):
        self.client_socket = None
        self.server_address = None
        self.server_port = None

    def connect(self):
        self.server_address = '127.0.0.1'
        self.server_port = 6699
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_address, self.server_port))
            # print(f"Connected to {self.server_address} on port {self.server_port}")
        except Exception as e:
            print(f"An error occurred in connecting: {e}")
            self.client_socket.close()
            self.client_socket = None
            return False
        return True

    def to_binary(self, skeleton_data):
        MAGIC_NUMBER_HEAD = 0xFFFFFFFF
        MAGIC_NUMBER_TAIL = 0xFFFFFFFE
        def pack_string(input_string):
            if len(input_string) > 64:
                input_string = input_string[:64]
            else:
                input_string = input_string.ljust(64, '\0')
            packed_string = struct.pack('64s', input_string.encode())

            return packed_string

        # buffer += pack_string(skeleton_data.name)
        buffer = struct.pack('I', MAGIC_NUMBER_HEAD)
        for bone in skeleton_data.bones:
            buffer += struct.pack('fff', *bone.translate)
            buffer += struct.pack('ffff', *bone.orientation)
        buffer += struct.pack('I', MAGIC_NUMBER_TAIL)
        print(len(buffer))
        return buffer

    def send_data(self, skeleton_data):
        if self.client_socket is None:
            return False
        try:
            skeleton_data = self.to_binary(skeleton_data)
            self.client_socket.sendall(skeleton_data)
        except Exception as e:
            print(f"An error occurred in sending: {e}")
            return False
        return True

    def close(self):
        if self.client_socket is not None:
            self.client_socket.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == '__main__':
    import time
    
    f = 0.0
    for i in range(10000):
        f += 1
        with TCPDataSender() as s:
            segments = []
            for j in range(34):
                segments.append(((0.0, 0.0, 0.0), (f, 100.0, 0.0)))
            sk_data = create_skeleton_data("Superman", segments)
            s.send_data(sk_data)
        time.sleep(0.1)
