import cv2
import mediapipe as mp
import time
import threading
from collections import deque
from collections import namedtuple
import numpy as np
import math
import vrfcam

point_3d = namedtuple('point_3d', ['x', 'y', 'z'])

k = 0.8
k2 = 1.1
std_p11p12_pose = 125 * k
std_p11p13_pose = 85.23 * k2
std_p13p15_pose = 83.8 * k2
std_p12p14_pose = 85.77 * k2
std_p14p16_pose = 73.11 * k2
std_p11p23_pose = 184.38
std_p12p24_pose = 176.537
std_p23p25_pose = 121.25 * 0.8
std_p24p26_pose = 118.05 * 0.8
std_p25p27_pose = 116.08 * 0.8
std_p26p28_pose = 121.25 * 0.8
std_p27p29_pose = 22.34
std_p28p30_pose = 23.18
std_p27p31_pose = 41.55
std_p28p32_pose = 54.39
std_p29p31_pose = 35.88
std_p30p32_pose = 34.1

k = 1
std_01_hand = 9.05 * k
std_05_hand = 30 * k
std_09_hand = 30.07 * k
std_013_hand = 28.31 * k
std_017_hand = 25.22 * k
std_12_hand = 11.95 * k
std_23_hand = 9.814 * k
std_34_hand = 7.865 * k
std_56_hand = 11.42 * k
std_59_hand = 4.966 * k
std_67_hand = 7.19 * k
std_78_hand = 6.47 * k
std_910_hand = 12.81 * k
std_913_hand = 4.7 * k
std_1011_hand = 8 * k
std_1112_hand = 6.937 * k
std_1314_hand = 11.74 * k
std_1317_hand = 5.757 * k
std_1415_hand = 7.517 * k
std_1516_hand = 7.053 * k
std_1718_hand = 8.747 * k
std_1819_hand = 5.958 * k
std_1920_hand = 5.754 * k
# tolerance_rate = 0.015
tolerance_rate = 0


def get_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def get_z(pxpx, std, std_xx):
    z = (std * std_xx / std_p11p23_pose) ** 2 - pxpx ** 2
    return math.sqrt(z) if z >= 0 else 0


def midpoint(pt1, pt2, a, b):
    mid_x = (a * pt1.x + (b - a) * pt2.x) / b
    mid_y = (a * pt1.y + (b - a) * pt2.y) / b
    mid_z = (a * pt1.z + (b - a) * pt2.z) / b
    new_point = point_3d(x=mid_x, y=mid_y, z=mid_z)
    return new_point


def get_bone_set(pts):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24,\
        p25, p26, p27, p28, p29, p30, p31, p32, p33 = [pts[i] for i in range(34)]
    list_start = [p0, p1, p2, p2, p4, p5, p6, p7, p8, p7, p2, p11, p12, p13, p14, p15, p14, p0, p18, p19, p20, p0, \
                  p22, p23, p24, p3, p26, p26, p26, p26, p26, p20, p24]
    list_end = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24,\
        p25, p26, p27, p28, p29, p30, p31, p32, p33]
    # list_start = list_start[::2]
    # list_end = list_end[::2]
    bone_set = [((a[0], a[1], a[2]), (b[0], b[1], b[2])) for a, b in zip(list_start, list_end)]
    
    return bone_set


def derive_pose_z(landmarks, landmarks_world):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32 = landmarks
    P0, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32 = landmarks_world
    p11p12_pose = get_distance(p11, p12)
    p11p13_pose = get_distance(p11, p13)
    p13p15_pose = get_distance(p13, p15)
    p12p14_pose = get_distance(p12, p14)
    p14p16_pose = get_distance(p14, p16)
    p11p23_pose = get_distance(p11, p23)
    p12p24_pose = get_distance(p12, p24)
    p23p25_pose = get_distance(p23, p25)
    p24p26_pose = get_distance(p24, p26)
    p25p27_pose = get_distance(p25, p27)
    p26p28_pose = get_distance(p26, p28)
    p27p29_pose = get_distance(p27, p29)
    p28p30_pose = get_distance(p28, p30)
    p27p31_pose = get_distance(p27, p31)
    p28p32_pose = get_distance(p28, p32)
    p29p31_pose = get_distance(p29, p31)
    p30p32_pose = get_distance(p30, p32)
    std_pose = p11p23_pose

    z1112 = get_z(p11p12_pose, std_pose, std_p11p12_pose)
    z1113 = get_z(p11p13_pose, std_pose, std_p11p13_pose)
    z1315 = get_z(p13p15_pose, std_pose, std_p13p15_pose)
    z1214 = get_z(p12p14_pose, std_pose, std_p12p14_pose)
    z1416 = get_z(p14p16_pose, std_pose, std_p14p16_pose)
    z1123 = get_z(p11p23_pose, std_pose, std_p11p23_pose)
    z1224 = get_z(p12p24_pose, std_pose, std_p12p24_pose)
    z2325 = get_z(p23p25_pose, std_pose, std_p23p25_pose)
    z2426 = get_z(p24p26_pose, std_pose, std_p24p26_pose)
    z2527 = get_z(p25p27_pose, std_pose, std_p25p27_pose)
    z2628 = get_z(p26p28_pose, std_pose, std_p26p28_pose)
    z2729 = get_z(p27p29_pose, std_pose, std_p27p29_pose)
    z2830 = get_z(p28p30_pose, std_pose, std_p28p30_pose)
    z2731 = get_z(p27p31_pose, std_pose, std_p27p31_pose)
    z2832 = get_z(p28p32_pose, std_pose, std_p28p32_pose)
    z2931 = get_z(p29p31_pose, std_pose, std_p29p31_pose)
    z3032 = get_z(p30p32_pose, std_pose, std_p30p32_pose)
    
    if P23.z >= P24.z * 0.9:
        z23, z24 = z1112 * 0.3, -z1112 * 0.3
    else:
        z23, z24 = -z1112 * 0.3, z1112 * 0.3
    z11 = z23 + z1123 if P11.z >= P23.z else z23 - z1123
    z12 = z24 + z1224 if P12.z >= P24.z else z24 - z1224
    z13 = z11 + z1113 if P13.z >= P11.z else z11 - z1113
    z15 = z13 + z1315 if P15.z >= P13.z else z13 - z1315
    z14 = z12 + z1214 if P14.z >= P12.z else z12 - z1214
    z16 = z14 + z1416 if P16.z >= P14.z else z14 - z1416
    z25 = z23 + z2325 if P25.z >= P23.z else z23 - z2325
    z26 = z24 + z2426 if P26.z >= P24.z else z24 - z2426
    z27 = z25 + z2527 if P27.z >= P25.z else z25 - z2527
    z28 = z26 + z2628 if P28.z >= P26.z else z26 - z2628
    z29 = z27 + z2729 if p29.z >= p27.z else z27 - z2729
    z30 = z28 + z2830 if P30.z >= P28.z else z28 - z2830
    z31 = z27 + z2731 if P31.z >= P27.z else z27 - z2731
    z32 = z28 + z2832 if P32.z >= P28.z else z28 - z2832
    
    p11.z, p12.z, p13.z, p14.z, p15.z, p16.z, p23.z, p24.z, p25.z, p26.z, p27.z, p28.z, p29.z, p30.z, p31.z, p32.z \
        = z11, z12, z13, z14, z15, z16, z23, z24, z25, z26, z27, z28, z29, z30, z31, z32
    
    p0.z, p1.z, p2.z, p3.z, p4.z, p5.z, p6.z, p7.z, p8.z, p9.z, p10.z = z11, z11, z11, z11, z11, z11, z11, z11, z11, z11, z11
    
    det_2324 = p24.y - p23.y
    p23.y, p24.y = p23.y + 0.5 * det_2324, p24.y - 0.5 * det_2324
    
    # det_1112 = p12.y - p11.y
    # p11.y, p12.y = p11.y + 0.5 * det_1112, p12.y + 0.5 * det_1112
    
    landmarks = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21,
                 p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32]
    
    return landmarks, std_pose, 


def derive_hand_z(landmarks, z_std, std_pose):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = landmarks
    p0p1_hand = get_distance(p0, p1)
    p0p5_hand = get_distance(p0, p5)
    p0p9_hand = get_distance(p0, p9)
    p0p13_hand = get_distance(p0, p13)
    p0p17_hand = get_distance(p0, p17)
    p1p2_hand = get_distance(p1, p2)
    p2p3_hand = get_distance(p2, p3)
    p3p4_hand = get_distance(p3, p4)
    p5p6_hand = get_distance(p5, p6)
    p5p9_hand = get_distance(p5, p9)
    p6p7_hand = get_distance(p6, p7)
    p7p8_hand = get_distance(p7, p8)
    p9p10_hand = get_distance(p9, p10)
    p9p13_hand = get_distance(p9, p13)
    p10p11_hand = get_distance(p10, p11)
    p11p12_hand = get_distance(p11, p12)
    p13p14_hand = get_distance(p13, p14)
    p13p17_hand = get_distance(p13, p17)
    p14p15_hand = get_distance(p14, p15)
    p15p16_hand = get_distance(p15, p16)
    p17p18_hand = get_distance(p17, p18)
    p18p19_hand = get_distance(p18, p19)
    p19p20_hand = get_distance(p19, p20)

    z0 = z_std
    z01 = get_z(p0p1_hand, std_pose, std_01_hand)
    z12 = get_z(p1p2_hand, std_pose, std_12_hand)
    z23 = get_z(p2p3_hand, std_pose, std_23_hand)
    z34 = get_z(p3p4_hand, std_pose, std_34_hand)
    z05 = get_z(p0p5_hand, std_pose, std_05_hand)
    z09 = get_z(p0p9_hand, std_pose, std_09_hand)
    z013 = get_z(p0p13_hand, std_pose, std_013_hand)
    z56 = get_z(p5p6_hand, std_pose, std_56_hand)
    z59 = get_z(p5p9_hand, std_pose, std_59_hand)
    z67 = get_z(p6p7_hand, std_pose, std_67_hand)
    z78 = get_z(p7p8_hand, std_pose, std_78_hand)
    z910 = get_z(p9p10_hand, std_pose, std_910_hand)
    z913 = get_z(p9p13_hand, std_pose, std_913_hand)
    z1011 = get_z(p10p11_hand, std_pose, std_1011_hand)
    z1112 = get_z(p11p12_hand, std_pose, std_1112_hand)
    z1314 = get_z(p13p14_hand, std_pose, std_1314_hand)
    z1317 = get_z(p13p17_hand, std_pose, std_1317_hand)
    z1415 = get_z(p14p15_hand, std_pose, std_1415_hand)
    z1516 = get_z(p15p16_hand, std_pose, std_1516_hand)
    z017 = get_z(p0p17_hand, std_pose, std_017_hand)
    z1718 = get_z(p17p18_hand, std_pose, std_1718_hand)
    z1819 = get_z(p18p19_hand, std_pose, std_1819_hand)
    z1920 = get_z(p19p20_hand, std_pose, std_1920_hand)

    z1 = z0 + z01 if p1.z - p0.z > tolerance_rate * std_01_hand else (
        z0 - z01 if p1.z - p0.z < -tolerance_rate * std_01_hand else z0)
    z2 = z1 + z12 if p2.z - p1.z > tolerance_rate * std_12_hand else (
        z1 - z12 if p2.z - p1.z < -tolerance_rate * std_12_hand else z1)
    z3 = z2 + z23 if p3.z - p2.z > tolerance_rate * std_23_hand else (
        z2 - z23 if p3.z - p2.z < -tolerance_rate * std_23_hand else z2)
    z4 = z3 + z34 if p4.z - p3.z > tolerance_rate * std_34_hand else (
        z3 - z34 if p4.z - p3.z < -tolerance_rate * std_34_hand else z3)
    z5 = z0 + z05 if p5.z - p0.z > tolerance_rate * std_05_hand else (
        z0 - z05 if p5.z - p0.z < -tolerance_rate * std_05_hand else z0)
    z6 = z5 + z56 if p6.z - p5.z > tolerance_rate * std_56_hand else (
        z5 - z56 if p6.z - p5.z < -tolerance_rate * std_56_hand else z5)
    z7 = z6 + z67 if p7.z - p6.z > tolerance_rate * std_67_hand else (
        z6 - z67 if p7.z - p6.z < -tolerance_rate * std_67_hand else z6)
    z8 = z7 + z78 if p8.z - p7.z > tolerance_rate * std_78_hand else (
        z7 - z78 if p8.z - p7.z < -tolerance_rate * std_78_hand else z7)
    z9_1 = z0 + z09 if p9.z - p0.z > tolerance_rate * std_09_hand else (
        z0 - z09 if p9.z - p0.z < -tolerance_rate * std_09_hand else z0)
    z9_2 = z5 + z59 if p9.z - p5.z > tolerance_rate * std_59_hand else (
        z5 - z59 if p9.z - p5.z < -tolerance_rate * std_59_hand else z5)
    z9 = z9_1 * 0.5 + z9_2 * 0.5
    z10 = z9 + z910 if p10.z - p9.z > tolerance_rate * std_910_hand else (
        z9 - z910 if p10.z - p9.z < -tolerance_rate * std_910_hand else z9)
    z11 = z10 + z1011 if p11.z - p10.z > tolerance_rate * std_1011_hand else (
        z10 - z1011 if p11.z - p10.z < -tolerance_rate * std_1011_hand else z10)
    z12 = z11 + z1112 if p12.z - p11.z > tolerance_rate * std_1112_hand else (
        z11 - z1112 if p12.z - p11.z < -tolerance_rate * std_1112_hand else z11)
    z13_1 = z0 + z013 if p13.z - p0.z > tolerance_rate * std_013_hand else (
        z0 - z013 if p13.z - p0.z < -tolerance_rate * std_013_hand else z0)
    z13_2 = z9 + z013 if p13.z - p9.z > tolerance_rate * std_913_hand else (
        z9 - z013 if p13.z - p9.z < -tolerance_rate * std_913_hand else z9)
    z13 = z13_1 * 0.5 + z13_2 * 0.5
    z14 = z13 + z1314 if p14.z - p13.z > tolerance_rate * std_1314_hand else (
        z13 - z1314 if p14.z - p13.z < -tolerance_rate * std_1314_hand else z13)
    z15 = z14 + z1415 if p15.z - p14.z > tolerance_rate * std_1415_hand else (
        z14 - z1314 if p15.z - p14.z < -tolerance_rate * std_1415_hand else z14)
    z16 = z15 + z1516 if p16.z - p15.z > tolerance_rate * std_1516_hand else (
        z15 - z1516 if p16.z - p15.z < -tolerance_rate * std_1516_hand else z15)
    z17_1 = z0 + z017 if p17.z - p0.z > tolerance_rate * std_017_hand else (
        z0 - z017 if p17.z - p0.z < -tolerance_rate * std_017_hand else z0)
    z17_2 = z13 + z1317 if p17.z - p13.z > tolerance_rate * std_1317_hand else (
        z13 - z1317 if p17.z - p13.z < -tolerance_rate * std_1317_hand else z13)
    z17 = z17_1 * 0.5 + z17_2 * 0.5
    z18 = z17 + z1718 if p18.z - p17.z > tolerance_rate * std_1718_hand else (
        z17 - z1718 if p18.z - p17.z < -tolerance_rate * std_1718_hand else z17)
    z19 = z18 + z1819 if p19.z - p18.z > tolerance_rate * std_1819_hand else (
        z18 - z1819 if p19.z - p18.z < -tolerance_rate * std_1819_hand else z18)
    z20 = z19 + z1920 if p20.z - p19.z > tolerance_rate * std_1920_hand else (
        z19 - z1920 if p20.z - p19.z < -tolerance_rate * std_1920_hand else z19)

    p0.z, p1.z, p2.z, p3.z, p4.z, p5.z, p6.z, p7.z, p8.z, p9.z, p10.z, p11.z, p12.z, p13.z, p14.z, p15.z, p16.z, p17.z, p18.z, p19.z, p20.z \
        = z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15, z16, z17, z18, z19, z20
    landmarks = p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20
    return landmarks


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
exit_flag = False


def get_point1(p18, p22, p2, len_p1123):
    z = 0
    len_p2324 = len_p1123 * 0.6
    mid_point = ((p18.x + p22.x) / 2, (p18.y + p22.y) / 2)
    direction_vector = np.array([p22.y - p18.y, -(p22.x - p18.x)])  # Perpendicular vector
    if p18.x > p22.x:
        direction_vector = - direction_vector

    unit_direction_vector = direction_vector / np.linalg.norm(direction_vector)
    c = mid_point + len_p2324 * unit_direction_vector
    x, y = c[0], c[1]
    
    return x, y, z
    

def get_34_points(landmarks, len_p1123):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32 = landmarks
    
    p34_0 = midpoint(p23, p24, 1, 2)
    p34_2 = midpoint(p11, p12, 1, 2)
    p34_1 = midpoint(p34_0, p34_2, 1, 2)
    # p34_1 = point_3d(x=p34_1.x, y=p34_1.y, z=0.5*p34_2.z)
    # p34_2 = midpoint(p34_0, p34_3, 4, 5)
    p34_3 = midpoint(p34_0, p34_2, -1, 6)
    p34_5 = point_3d(x=p11.x, y=p11.y, z=p11.z)
    p34_4 = midpoint(p34_2, p34_5, 1, 2)
    p34_6 = point_3d(x=p13.x, y=p13.y, z=p13.z)
    p34_7 = point_3d(x=p15.x, y=p15.y, z=p15.z)
    p34_9 = midpoint(p17, p19, 1, 2)
    p34_8 = midpoint(p34_7, p34_9, 1, 2)
    p34_10 = point_3d(x=p21.x, y=p21.y, z=p21.z)
    p34_12 = point_3d(x=p12.x, y=p12.y, z=p12.z)
    p34_11 = midpoint(p34_2, p34_12, 1, 2)
    p34_13 = point_3d(x=p14.x, y=p14.y, z=p14.z)
    p34_14 = point_3d(x=p16.x, y=p16.y, z=p16.z)
    p34_16 = midpoint(p18, p20, 1, 2)
    p34_15 = midpoint(p34_14, p34_16, 1, 2)
    p34_17 = point_3d(x=p22.x, y=p22.y, z=p22.z)
    p34_18 = point_3d(x=p23.x, y=p23.y, z=p23.z)
    p34_19 = point_3d(x=p25.x, y=p25.y, z=p25.z)
    p34_20 = point_3d(x=p27.x, y=p27.y, z=p27.z)
    p34_21 = point_3d(x=p31.x, y=p31.y, z=p31.z)
    p34_22 = point_3d(x=p24.x, y=p24.y, z=p24.z)
    p34_23 = point_3d(x=p26.x, y=p26.y, z=p26.z)
    p34_24 = point_3d(x=p28.x, y=p28.y, z=p28.z)
    p34_25 = point_3d(x=p32.x, y=p32.y, z=p32.z)
    p34_26 = point_3d(x=p0.x, y=p0.y, z=p0.z)
    p34_27 = point_3d(x=p0.x, y=p0.y, z=p0.z)
    p34_28 = point_3d(x=p2.x, y=p2.y, z=p2.z)
    p34_29 = point_3d(x=p7.x, y=p7.y, z=p7.z)
    p34_30 = point_3d(x=p5.x, y=p5.y, z=p5.z)
    p34_31 = point_3d(x=p8.x, y=p8.y, z=p8.z)
    p34_32 = point_3d(x=p29.x, y=p29.y, z=p29.z)
    p34_33 = point_3d(x=p30.x, y=p30.y, z=p30.z)
    
    
    points_34 = np.array([p34_0, p34_1, p34_2, p34_3, p34_11, p34_12, p34_13, p34_14, p34_15, p34_16, p34_17, p34_4, p34_5, p34_6, \
                 p34_7, p34_8, p34_9, p34_10, p34_22, p34_23, p34_24, p34_25, p34_18, p34_19, p34_20, p34_21, p34_26, \
                 p34_27, p34_30, p34_31, p34_28, p34_29, p34_33, p34_32])
    # points_34 = np.array([p34_0, p34_1, p34_2, p34_3, p34_4, p34_5, p34_6, p34_7, p34_8, p34_9, p34_10, p34_11, p34_12, p34_13, \
    #              p34_14, p34_15, p34_16, p34_17, p34_18, p34_19, p34_20, p34_21, p34_22, p34_23, p34_24, p34_25, p34_26, \
    #              p34_27, p34_28, p34_29, p34_30, p34_31, p34_32, p34_33])
    
    return points_34


pose_connections = frozenset([(11, 12), (11, 13),
                              (13, 15), (15, 17), (15, 19), (15, 21), (17, 19),
                              (12, 14), (14, 16), (16, 18), (16, 20), (16, 22),
                              (18, 20), (11, 23), (12, 24), (23, 24), (23, 25),
                              (24, 26), (25, 27), (26, 28), (27, 29), (28, 30),
                              (29, 31), (30, 32), (27, 31), (28, 32)])


# For webcam input:
cap = cv2.VideoCapture(0)
desired_width = 640
desired_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)
# cap.set(cv2.CAP_PROP_EXPOSURE, 0)

previous_left_hand_landmarks = None
previous_right_hand_landmarks = None
num_left = 0
num_right = 0

g_queue = deque(maxlen=2)
g_lock = threading.Lock()
g_output = deque(maxlen=6)
g_output_lock = threading.Lock()


def get_image_loop():
    global exit_flag
    while cap.isOpened() and not exit_flag:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        if not success:
            print("Ignoring empty camera frame.")
            continue
        with g_lock:
            g_queue.append(image)


holistic = mp_holistic.Holistic(
    # static_image_mode=True,
    model_complexity=2,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,

)



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


def quaternion_multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2

    return np.array([w, x, y, z])


def get_all_quaternions(points_34):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, \
        p25, p26, p27, p28, p29, p30, p31, p32, p33 = points_34
    
    stdv_horizontal = np.array((0, 1, 0))
    stdv_vertical = np.array((0, 0, 1))
    stdv_depth = np.array((1, 0, 0))
    stdv_lthumb = np.array((1, -1, 0))
    stdv_rthumb = np.array((1, 1, 0))
    
    v1 = p1 - p0
    v2 = p2 - p1
    v3 = p3 - p2
    v4 = p4 - p2
    v5 = p5 - p2
    v6 = p6 - p5
    v7 = p7 - p6
    v8 = p8 - p7
    v8_10 = p10 - p8
    v9 = p9 - p8
    v10 = p10 - p7
    v11 = p11 - p2
    v12 = p12 - p2
    v13 = p13 - p12
    v14 = p14 - p13
    v15 = p15 - p14
    v16 = p16 - p15
    v17 = p17 - p14
    v18 = p18 - p0
    v19 = p19 - p18
    v20 = p20 - p19
    v21 = p21 - p20
    v22 = p22 - p0
    v23 = p23 - p22
    v24 = p24 - p23
    v25 = p25 - p24
    v26 = p26 - p2
    
    v27 = p27 - p26
    v28 = p28 - p27
    v29 = p29 - p28
    v30 = p30 - p27
    v31 = p31 - p30
    
    v32 = p32 - p20
    v33 = p33 - p24
    
    rq0_1 = quaternion_from_two_vectors(stdv_vertical, v1)
    rq0_22 = quaternion_from_two_vectors(stdv_horizontal, v22)
    rq0 = quaternion_multiply(rq0_22, rq0_1)
    rq1_2 = quaternion_from_two_vectors(v1, v2)
    rq2_3 = quaternion_from_two_vectors(stdv_vertical, v2)
    rq4_5 = (1, 0, 0, 0)
    rq2_4 = (1, 0, 0, 0)
    rq2_5 = quaternion_from_two_vectors(v4, -stdv_horizontal)
    rq5_6 = quaternion_from_two_vectors(-stdv_horizontal, v6)
    rq5 = quaternion_multiply(rq2_5, rq5_6)
    rq6_7 = quaternion_from_two_vectors(v6, v7)
    # rq7_s = quaternion_from_two_vectors(v7, stdv_horizontal)
    # rqs_8 = quaternion_from_two_vectors(stdv_horizontal, v9)
    # rq7 = quaternion_multiply(rq7_s, rqs_8)
    rq7 = (1, 0, 0, 0)
    rq8_9 = quaternion_from_two_vectors(v8, v9)
    rq8_10 = quaternion_from_two_vectors(stdv_depth, v8_10)
    # rq2_11 = quaternion_from_two_vectors(v2, v11)
    rq2_11 = (1, 0, 0, 0)
    rq11_12 = (1, 0, 0, 0)
    rq2_12 = quaternion_from_two_vectors(v11, stdv_horizontal)
    rq12_13 = quaternion_from_two_vectors(stdv_horizontal, v13)
    rq12 = quaternion_multiply(rq2_12, rq12_13)
    rq13_14 = quaternion_from_two_vectors(v13, v14)
    # rq14_15 = quaternion_from_two_vectors(v14, v15)
    rq14_15 = (1, 0, 0, 0)
    rq15_16 = quaternion_from_two_vectors(v15, v16)
    rq14_17 = quaternion_from_two_vectors(v14, v17)
    # rq0_18 = quaternion_from_two_vectors(stdv_horizontal, v18)
    rq0_18 = (1, 0, 0, 0)
    rq18_19 = quaternion_from_two_vectors(-v1, v19)
    rq19_20 = quaternion_from_two_vectors(v19, v20)
    # rq20_21 = quaternion_from_two_vectors(stdv_depth, v21)
    rq20_21 = (1, 0, 0, 0)
    rq0_22 = (1, 0, 0, 0)
    rq22_23 = quaternion_from_two_vectors(-v1, v23)
    rq23_24 = quaternion_from_two_vectors(v23, v24)
    # rq24_25 = quaternion_from_two_vectors(stdv_depth, v25)
    rq24_25 = (1, 0, 0, 0)
    rq3_26 = quaternion_from_two_vectors(v3, v26)
    rq3_26 = (1, 0, 0, 0)
    rq3_27 = quaternion_from_two_vectors(v3, v27)
    rq27_28 = quaternion_from_two_vectors(v27, v28)
    rq28_29 = quaternion_from_two_vectors(v28, v29)
    rq27_30 = quaternion_from_two_vectors(v27, v30)
    rq30_31 = quaternion_from_two_vectors(v30, v31)
    rq20_32 = (1, 0, 0, 0)
    rq24_33 = (1, 0, 0, 0)
    rq24_34 = (1, 0, 0, 0)
    
    rqs = np.array([rq0, rq1_2, rq2_3, rq2_4, rq4_5, rq5, rq6_7, rq7, rq8_9, rq8_10, rq2_11, rq11_12, rq12,
                    rq13_14, rq14_15, rq15_16, rq14_17, rq0_18, rq18_19, rq19_20, rq20_21, rq0_22, rq22_23, rq23_24, rq24_25,
                    rq3_27, rq3_27, rq3_27, rq28_29, rq27_30, rq30_31, rq20_32, rq24_33, rq24_34])
    
    return rqs

    
    
frame_num = 0

points_queue = deque(maxlen=2)
def handle_result():
    global frame_num, exit_flag
    while not exit_flag:
        t0 = time.time()
        with g_output_lock:
            if len(g_output) > 0:
                image, results = g_output.popleft()
            else:
                continue
        if results is None:
            continue
        frame_num += 1
        # print(f"frame number:{frame_num}")
        pose_results = results.pose_landmarks
        pose_results_world = results.pose_world_landmarks
        if pose_results and pose_results_world is not None:
            for landmark in pose_results.landmark:
                x, y, z = landmark.x * 640, landmark.y * 480, landmark.z
                landmark.x, landmark.y = x, y
            pose_landmark_3d, len_p11p23 = derive_pose_z(pose_results.landmark, pose_results_world.landmark)
            
            points_34 = get_34_points(pose_landmark_3d, len_p11p23)
            points_34 = np.array([(-point[2], point[0] - 320, 280 - point[1]) for point in points_34])
            points_queue.append(points_34)
            if len(points_queue) > 1:
                points_34 = np.mean(points_queue, axis=0)
            bone_set = get_bone_set(points_34)
            
            orientations = get_all_quaternions(points_34)
            translations = points_34
            # cv2.imshow('Camera Feed', image)
            with vrfcam.TCPDataSender() as s:
                segments = bone_set
                sk_data = vrfcam.create_skeleton_data1("Superman", segments, translations, orientations)
                s.send_data(sk_data)
            
        if cv2.waitKey(5) & 0xFF == 27:
            exit_flag = True
            break
        t = time.time() - t0
        # print(1/t)
    

def process_image_loop():
    while not exit_flag:
        with g_lock:
            if len(g_queue) > 0:
                image = g_queue.popleft()
            else:
                continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        with g_output_lock:
            g_output.append((image, results))


t1 = threading.Thread(target=get_image_loop)
pros_ths = [threading.Thread(target=process_image_loop) for _ in range(1)]
t4 = threading.Thread(target=handle_result)

t1.start()
t4.start()
for th in pros_ths:
    th.start()

t1.join()

cv2.destroyAllWindows()

