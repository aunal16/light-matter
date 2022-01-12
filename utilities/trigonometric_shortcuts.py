import numpy as np


def sind(x):
    return np.sin(x * np.pi / 180)


def cosd(x):
    return np.cos(x * np.pi / 180)


def tand(x):
    return np.tan(x * np.pi / 180)


def asind(x):
    return np.arcsin(x) * 180 / np.pi


def acosd(x):
    return np.arccos(x) * 180 / np.pi


def atand(x):
    return np.arctan(x) * 180 / np.pi
