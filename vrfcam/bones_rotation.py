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

s = 0.25
std_p11p12_pose = 125
std_p11p13_pose = 85.23
std_p13p15_pose = 83.8
std_p12p14_pose = 85.77
std_p14p16_pose = 73.11
std_p11p23_pose = 184.38
std_p12p24_pose = 176.537
std_p23p25_pose = 121.25
std_p24p26_pose = 118.05
std_p25p27_pose = 116.08
std_p26p28_pose = 121.25
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


# def get_z(pxpx, std, std_xx, std_p11p23_pose):
def get_z(pxpx, std, std_xx):
    # z = std_xx ** 2 - (pxpx / std * std_xx) ** 2
    z = (std * std_xx / std_p11p23_pose) ** 2 - pxpx ** 2
    return math.sqrt(z) if z >= 0 else 0


def midpoint(pt1, pt2, a, b):
    mid_x = (a * pt1.x + (b - a) * pt2.x) / b
    mid_y = (a * pt1.y + (b - a) * pt2.y) / b
    mid_z = (a * pt1.z + (b - a) * pt2.z) / b
    new_point = point_3d(x=mid_x, y=mid_y, z=mid_z)
    return new_point


def get_bone_set(pts):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, \
        p25, p26, p27, p28, p29, p30, p31, p32, p33 = [pts[i] for i in range(34)]
    list_start = [p0, p1, p2, p2, p4, p5, p6, p7, p8, p7, p2, p11, p12, p13, p14, p15, p14, p0, p18, p19, p20, p0, \
                  p22, p23, p24, p3, p26, p26, p26, p26, p26, p20, p24]
    list_end = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22,
                p23, p24, \
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
    # if p11.z >= p12.z * 1.15:
    if P11.z >= P12.z * 1.0:
        z11, z12 = z1112 * 0.5, -z1112 * 0.5
    else:
        z11, z12 = -z1112 * 0.5, z1112 * 0.5
    z13 = z11 + z1113 if P13.z >= P11.z else z11 - z1113
    z15 = z13 + z1315 if P15.z >= P13.z else z13 - z1315
    z14 = z12 + z1214 if P14.z >= P12.z else z12 - z1214
    z16 = z14 + z1416 if P16.z >= P14.z else z14 - z1416
    z23 = z11 + z1123 if P23.z >= P11.z else z11 - z1123
    z24 = z12 + z1224 if P24.z >= P12.z else z12 - z1224
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

    landmarks = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21,
                 p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32]

    return landmarks


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


def get_pixel_coordinates(landmark, width, height):
    x = int(landmark.x * width)
    y = int(landmark.y * height)
    return x, y


def get_34_points(landmarks):
    p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32 = landmarks
    p34_0 = midpoint(p23, p24, 1, 2)
    p34_2 = midpoint(p11, p12, 1, 2)
    p34_1 = midpoint(p34_0, p34_2, 2, 5)
    # p34_2 = midpoint(p34_0, p34_3, 4, 5)
    p34_3 = midpoint(p34_0, p34_2, 7, 6)
    p34_5 = point_3d(x=p11.x, y=p11.y, z=p11.z)
    p34_4 = midpoint(p34_2, p34_5, 1, 2)
    p34_6 = point_3d(x=p13.x, y=p13.y, z=p13.z)
    p34_7 = point_3d(x=p15.x, y=p15.y, z=p15.z)
    p34_8 = midpoint(p15, p19, 1, 2)
    p34_9 = point_3d(x=p19.x, y=p19.y, z=p19.z)
    p34_10 = point_3d(x=p21.x, y=p21.y, z=p21.z)
    p34_12 = point_3d(x=p12.x, y=p12.y, z=p12.z)
    p34_11 = midpoint(p34_2, p34_12, 1, 2)
    p34_13 = point_3d(x=p14.x, y=p14.y, z=p14.z)
    p34_14 = point_3d(x=p16.x, y=p16.y, z=p16.z)
    p34_15 = midpoint(p16, p20, 1, 2)
    p34_16 = point_3d(x=p20.x, y=p20.y, z=p20.z)
    p34_17 = point_3d(x=p22.x, y=p22.y, z=p22.z)
    p34_18 = point_3d(x=p23.x, y=p23.y, z=p23.z)
    p34_19 = point_3d(x=p25.x, y=p25.y, z=p25.z)
    p34_20 = point_3d(x=p27.x, y=p27.y, z=p27.z)
    p34_21 = point_3d(x=p31.x, y=p31.y, z=p31.z)
    p34_22 = point_3d(x=p24.x, y=p24.y, z=p24.z)
    p34_23 = point_3d(x=p26.x, y=p26.y, z=p26.z)
    p34_24 = point_3d(x=p28.x, y=p28.y, z=p28.z)
    p34_25 = point_3d(x=p32.x, y=p32.y, z=p32.z)
    p34_26 = midpoint(p34_3, p0, 1, 2)
    p34_27 = point_3d(x=p0.x, y=p0.y, z=p0.z)
    p34_28 = point_3d(x=p2.x, y=p2.y, z=p2.z)
    p34_29 = point_3d(x=p7.x, y=p7.y, z=p7.z)
    p34_30 = point_3d(x=p5.x, y=p5.y, z=p5.z)
    p34_31 = point_3d(x=p8.x, y=p8.y, z=p8.z)
    p34_32 = point_3d(x=p29.x, y=p29.y, z=p29.z)
    p34_33 = point_3d(x=p30.x, y=p30.y, z=p30.z)

    # points_34 = np.array([p34_0, p34_1, p34_2, p34_3, p34_4, p34_5, p34_6, p34_7, p34_8, p34_9, p34_10, p34_11, p34_12, p34_13, \
    #              p34_14, p34_15, p34_16, p34_17, p34_18, p34_19, p34_20, p34_21, p34_22, p34_23, p34_24, p34_25, p34_26, \
    #              p34_27, p34_28, p34_29, p34_30, p34_31, p34_32, p34_33]) - p34_0

    # points_34 = np.array([p34_0, p34_1, p34_2, p34_3, p34_4, p34_5, p34_6, p34_7, p34_8, p34_9, p34_10, p34_11, p34_12, p34_13, \
    #              p34_14, p34_15, p34_16, p34_17, p34_18, p34_19, p34_20, p34_21, p34_22, p34_23, p34_24, p34_25, p34_26, \
    #              p34_27, p34_28, p34_29, p34_30, p34_31, p34_32, p34_33])

    points_34 = np.array(
        [p34_0, p34_1, p34_2, p34_3, p34_11, p34_12, p34_13, p34_14, p34_15, p34_16, p34_17, p34_4, p34_5, p34_6, \
         p34_7, p34_8, p34_9, p34_10, p34_22, p34_23, p34_24, p34_25, p34_18, p34_19, p34_20, p34_21, p34_26, \
         p34_27, p34_30, p34_31, p34_28, p34_29, p34_33, p34_32])

    # print(p34_0, "p34_0")
    # print(p34_1, "p34_1")
    # print(p34_2, "p34_2")
    # # print(p34_3, "p34_3")
    # print(p34_4, "p34_4")
    # print(p34_5, "p34_5")
    # print(p34_6, "p34_6")
    # print(p34_7, "p34_7")

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
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,

)


def draw_landmarks(image, results):
    global frame_num, num_left, num_right, previous_right_hand_landmarks, previous_left_hand_landmarks
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style()
    )

    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        pose_connections,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
    )

    if results.left_hand_landmarks:
        previous_left_hand_landmarks = results.left_hand_landmarks
        num_left = 0
    elif num_left < 3:
        num_left += 1
    else:
        previous_left_hand_landmarks = None

    mp_drawing.draw_landmarks(
        image,
        previous_left_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_left_hand_landmarks_style()
    )

    if results.right_hand_landmarks:
        previous_right_hand_landmarks = results.right_hand_landmarks
        num_right = 0
    elif num_right < 3:
        num_right += 1
    else:
        previous_right_hand_landmarks = None
    mp_drawing.draw_landmarks(
        image,
        previous_right_hand_landmarks,
        mp_holistic.HAND_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_right_hand_landmarks_style()
    )


frame_num = 0


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
            pose_landmark_3d = derive_pose_z(pose_results.landmark, pose_results_world.landmark)
            points_34 = get_34_points(pose_landmark_3d)
            bone_set = get_bone_set(points_34)
            scale1, scale2 = 4, 20
            scaled_bone_set = [
                (
                    (-point1[2] / scale1, point1[0] / scale1, (point1[1]) / scale1),
                    (-point2[2] / scale1, point2[0] / scale1, (point2[1]) / scale1)
                )
                for point1, point2 in bone_set
            ]

            with vrfcam.TCPDataSender() as s:
                segments = scaled_bone_set
                sk_data = vrfcam.create_skeleton_data("Superman", segments)
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

