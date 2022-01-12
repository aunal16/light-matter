import numpy as np


def sind(x):
    # sine in degrees
    return np.sin(x * np.pi / 180)


def cosd(x):
    # cosine in degrees
    return np.cos(x * np.pi / 180)


def tand(x):
    # tangent in degrees
    return np.tan(x * np.pi / 180)


def asind(x):
    # arcsine in degrees
    return np.arcsin(x) * 180 / np.pi


def acosd(x):
    # arccosine in degrees
    return np.arccos(x) * 180 / np.pi


def atand(x):
    # arctangent in degrees
    return np.arctan(x) * 180 / np.pi
