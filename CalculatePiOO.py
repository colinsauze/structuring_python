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


class CalculatePiOO:
    '''
    Class for containing all the pi calculation functions
    '''
    def __init__(self):
        '''
        class constructor, automatically called when an instance is created
        '''
        # seed the random number generator so we always get the same answer
        np.random.seed(2017)

    # declared as a static method as we depend on anything else in the class
    @staticmethod
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

    # all non-static methods take self as the first parameter
    def calculate_pi(self, num_points):
        '''
        Calculates pi, takes the number of points to use as a parameter.
        Returns the value of pi which was calculated.
        '''
        inside_circle_count = self.generate_points(num_points)
        # get how many points were found inside the circle
        return 4.0 * (inside_circle_count / float(num_points))


if __name__ == '__main__':
    # get an instance of the CalculatePiOO class
    PI = CalculatePiOO()
    N = 10000
    print("pi is %f from %d samples" % (PI.calculate_pi(N), N))
