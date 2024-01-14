import socket
import struct
import numpy as np
import math


def points_to_orientation(pt1, pt2):
    # Base point
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2

    # Vector representing the direction of the line segment
    direction = np.array([x2 - x1, y2 - y1, z2 - z1])
    direction = direction / np.linalg.norm(direction)  # Normalize

    # Default reference vector (along the x-axis)
    reference = np.array([1.0, 0.0, 0.0])

    # Calculate quaternion
    axis = np.cross(reference, direction)
    angle = math.acos(np.dot(reference, direction))
    s = math.sin(angle / 2)
    x, y, z = axis * s
    w = math.cos(angle / 2)

    # Normalize quaternion
    norm = math.sqrt(x**2 + y**2 + z**2 + w**2)
    orientation = (x / norm, y / norm, z / norm, w / norm)

    return pt1, orientation




class Bone:
    def __int__(self):
        self.translate = (0.0, 0.0)
        self.orientation = (0.0, 0.0, 0.0, 0.0)


class SkeletonData:
    """
     - VRFusionSuperMan
     - [
         Bone x 34 /2 
       ]
    """
    def __init__(self, name):
        self.name = name
        self.bones = []

    def add_bone(self, bone):
        self.bones.append(bone)


def create_skeleton_data(role_name, segments):
    data = SkeletonData(role_name)
    for pt1, pt2 in segments:
        bone = Bone()
        bone.translate, bone.orientation = points_to_orientation(pt1, pt2)
        data.bones.append(bone)
    return data


class TCPDataSender:
    def __int__(self):
        self.client_socket = None
        self.server_address = None
        self.server_port = None

    def connect(self):
        self.server_address = '127.0.0.1'
        self.server_port = 6699
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.server_address, self.server_port))
            print(f"Connected to {self.server_address} on port {self.server_port}")
        except Exception as e:
            print(f"An error occurred in connecting: {e}")
            self.client_socket.close()
            self.client_socket = None
            return False
        return True
    
    def to_binary(self, skeleton_data):
        def pack_string(input_string):
            if len(input_string) > 64:
                input_string = input_string[:64]
            else:
                input_string = input_string.ljust(64, '\0')
            packed_string = struct.pack('64s', input_string.encode())

            return packed_string
        buffer = b''
        #buffer += pack_string(skeleton_data.name)
        for bone in skeleton_data.bones:
            buffer += struct.pack('fff', *bone.translate)
            buffer += struct.pack('ffff', *bone.orientation)
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

    for i in range(10000):
        with TCPDataSender() as s:
            segments = []
            for i in range(17):
                segment = [(i * 1.0, i * 1.0, i * 1.0), ((i + 1) * 1.0, (i + 1) * 1.0, (i + 1) * 1.0)]
                segments.append(segment)

            sk_data = create_skeleton_data("Superman", segments)
            s.send_data(sk_data)
        time.sleep(0.5)
