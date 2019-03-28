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
import numpy as np

# pylint: disable=no-member

# seed the random number generator so we always get the same answer
np.random.seed(2017)


def generate_points(num_points):
    '''
    Generates a set of random points, tests which are inside a circle.
    Takes number of points to generate as a parameter, returns the number
    inside the circle.
    '''
    x_coords = np.float32(np.random.uniform(size=num_points))
    y_coords = np.float32(np.random.uniform(size=num_points))

    radii = np.sqrt((x_coords**2)+(y_coords**2))

    # count how many points are in the circle,
    # they will be in the circle if x^2 + y^2 is less than 1.0
    filtered = np.where(radii <= 1.0)

    inside_circle_count = len(radii[filtered])
    return inside_circle_count


def calculate_pi(num_points):
    '''
    Calculates pi, takes the number of points to calculate with as a parameter.
    Returns the value of pi which was calculated.
    '''
    inside_circle_count = generate_points(num_points)
    # get how many points were found inside the circle
    return (4.0 * (inside_circle_count / float(num_points)))


if __name__ == '__main__':
    n_samples = 10000
    pi = calculate_pi(n_samples)
    print("pi is %f from %d samples" % (pi, n_samples))
