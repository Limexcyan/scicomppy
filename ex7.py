import itertools
import random

from ex6 import Vector

# Exercie 7.1


def find_axis(v1, v2):
    v3 = v1.cross(v2)
    L = v3.length()

    if L == 0:
        raise ValueError("Vectors are parallel or zero; no unique axis exists.")

    return Vector(v3.x / L, v3.y / L, v3.z / L)


v1 = Vector(1, 0, 0)
v2 = Vector(0, 1, 0)
print(find_axis(v1, v2))

# Exercise 7.2

# (a)


def boolean_series():
    while True:
        yield 0
        yield 1


# (b)


def random_boolean_series():
    while True:
        yield random.randint(0, 1)


# (c)


def sinkpi2series():
    while True:
        for val in [0, 1, 0, -1]:
            yield val
