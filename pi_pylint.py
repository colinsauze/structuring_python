#!/usr/bin/env python3
"""
Program to calculate Pi using a montecarlo method. This is based on the idea of
Buffon's Needle (https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)
A series of needles are dropped on a quarter circle drawn inside a square.
We count the number inside the circle and in total. The number of points in the
circle divided by the total number of points will give us an approximation for
pi/4 (as we only use a quarter circle) multiply this by 4 and we'll get an
approximation for pi increasing the number of points increases the accuracy to
a point, but gives diminishing returns over 10000 points
"""
import sys
import numpy as np

# pylint: disable=no-member

# seed the random number generator so we always get the same answer
np.random.seed(2017)


def generate_points():
    '''
    generates a set of random points, tests which are inside a circle
    '''
    x_coords = np.float32(np.random.uniform(size=10000))
    y_coords = np.float32(np.random.uniform(size=10000))

    radii = np.sqrt((x_coords**2)+(y_coords*y_coords))

    # count how many points are in the circle,
    # they will be in the circle if x^2 + y^2 is less than 1.0
    filtered = np.where(radii <= 1.0)

    inside_circle_count = len(radii[filtered])
    return inside_circle_count


def calculate_pi(numpoints):
    '''
    calculates pi
    '''
    inside_circle_count = generate_points()
    # get how many points were found inside the circle

    print("pi is %f" % (4.0 * (inside_circle_count / float(10000))),
          "from ", numpoints, " samples")


calculate_pi(10000)

sys.exit(1)
