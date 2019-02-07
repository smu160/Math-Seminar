"""
This module contains the Robot class and the arm linkage helper class, Linkage

@authors Saveliy Yusufov and Kohtaro Yamakawa
"""

import math
from operator import add


class Linkage:
    """A helper class for Robot"""

    def __init__(self, x_1, y_1, x_2, y_2):
        self.start = [x_1, y_1]
        self.end = [x_2, y_2]

    def get_length(self):
        """Compute the length of the linkage"""
        x = self.start[1] - self.start[0]
        y = self.end[1] - self.end[0]
        length = math.sqrt(x**2 + y**2)
        return length

class Robot:
    """A robot with at most 2 arm linkages"""

    def __init__(self, origin, radius):
        self.radius = radius

        x_1, y_1 = origin
        self.alpha = math.radians(0)
        x_2 = x_1 + 4 * radius * math.cos(self.alpha)
        y_2 = y_1 + 4 * radius * math.sin(self.alpha)

        self.link1 = Linkage(x_1, y_1, x_2, y_2)

        self.theta = math.radians(0)
        x_1 = self.link1.end[0]
        y_1 = self.link1.end[1]
        x_2 = x_1 + 2 * radius * math.cos(self.theta)
        y_2 = y_1 + 2 * radius * math.cos(self.theta)

        self.link2 = Linkage(x_1, y_1, x_2, y_2)

    def update_alpha(self, degrees):
        """Updates the angle

        Args:
            degrees: int
                The angle, in degrees!!!
        """
        self.alpha = math.radians(degrees)

    def update_theta(self, degrees):
        """Updates the angle

        Args:
            degrees: int
                The angle, in degrees!!!
        """
        self.theta = math.radians(degrees)

    def update_link1_pos(self):
        """Updates the end-point position of an arm linkage"""
        self.link1.end[0] = self.link1.start[0] + 4 * self.radius * math.cos(self.alpha)
        self.link1.end[1] = self.link1.start[1] + 4 * self.radius * math.sin(self.alpha)

    def update_link2_pos(self):
        """Updates the position of the second arm linkage"""
        self.link2.start[0] = self.link1.end[0]
        self.link2.start[1] = self.link1.end[1]
        self.link2.end[0] = self.link2.start[0] + 2 * self.radius * math.cos(self.theta)
        self.link2.end[1] = self.link2.start[1] + 2 * self.radius * math.sin(self.theta)

    def get_link1_pos(self):
        """Computes the position of the first arm linkage"""
        length = self.link1.get_length()
        c_alpha = math.cos(self.alpha)
        s_alpha = math.sin(self.alpha)
        pos = [length*c_alpha, length*s_alpha]
        return pos

    def get_link2_pos(self):
        """Computes the position of the first arm linkage"""
        length = self.link2.get_length()
        c_theta = math.cos(self.theta)
        s_theta = math.sin(self.theta)
        pos = [length*c_theta, length*s_theta]
        return pos

    def compute_xy(self):
        vec_1 = self.get_link1_pos()
        vec_2 = self.get_link2_pos()
        pos = list(map(add, vec_1, vec_2))
        return pos

    def get_pos(self):
        """Returns the angles of the linkages"""
        return self.alpha, self.theta
