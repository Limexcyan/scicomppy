# Exercise 6.1

import math


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # return string "Vector(x, y, z)"
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        # v == w
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):  # v != w
        return not self == other

    def __add__(self, other):
        # u + v
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    # Hint: return Vector(...)

    def __sub__(self, other):
        # v - w
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        # return the dot product (number)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        # return the cross product (Vector)
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def length(self):
        # the length of the vector
        return math.hypot(self.x, self.y, self.z)

    def __hash__(self):  # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))


# Exemplary tests

v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")
# two vectors are given (a vector is a 3-tuple in this reminder)
# a = (a1, a2, a3)
# b = (b1, b2, b3)
# the dot product (the result is a number)
# a · b = a1 * b1 + a2 * b2 + a3 * b3
# the cross product (the result is a vector)
# a × b = (a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
