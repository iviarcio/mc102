#!/usr/bin/env python3

"""vector.py: A simple little Vector class. Enabling basic vector math. """

__author__ = "Marcio Pereira"
__license__ = "GPL"
__version__ = "1.0"

from math import sqrt


class Vector:
    """Represents a Vector."""

    def __init__(self, x, y):
        """Constructor creates a Vector with x-axes and y-axes values."""
        self.x = x
        self.y = y

    def __str__(self):
        """ Return a string representation of self."""
        return "Vector(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):
        """ Return the sum of self and Vector object other."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Return the difference of self and Vector object other."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, alpha):
        """ Return the product of self and numeric object alpha."""
        return Vector(self.x * alpha, self.y * alpha)

    def __rmul__(self, alpha):
        """ Return the reverse product of self and numeric object alpha."""
        return Vector(self.x * alpha, self.y * alpha)

    def __truediv__(self, alpha):
        """ Return the division of self and numeric object alpha."""
        return Vector(self.x / alpha, self.y / alpha)

    def magnitude(self):
        """ Return the magnitude of self object."""
        return sqrt(self.x ** 2 + self.y ** 2)

    def norm(self):
        """ Return the self object normalized."""
        return self / self.magnitude()


# for testing: create and use some Vector objects
if __name__ == '__main__':
    v1 = Vector(3, 4)
    v2 = Vector(2, -1)
    v3 = Vector(-15, 3)
    print(v1.magnitude())
    print(v1.norm())
