from math import *


def cot(x):
    return 1/tan(x)


def dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return sqrt(x * x + y * y)