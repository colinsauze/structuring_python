#!/usr/local/bin/python2.56
import sys
"""
Program to calculate Pi using a montecarlo method. This is based on the idea of Buffon's Needle (https://en.wikipedia.org/wiki/Buffon%27s_needle_problem)
A series of needles are dropped on a quarter circle drawn inside a square. We count the number inside the circle and in total.
the number of points in the circle divided by the total number of points will give us an approximation for pi/4 (as we only use a quarter circle)
multiply this by 4 and we'll get an approximation for pi
increasing the number of points increases the accuracy to a point, but gives diminishing returns over 10000 points

This version of the program is hiddeously formatted, violates many Python conventions and the PEP8 coding standards.
Try to clean it up so it meets PEP8.

Thanks for everyone on the UKRSE slack channel for their suggestions about how to make this code extra hiddeous.
"""
import random
from numpy import *
import numpy as np
#seed the random number generator so we always get the same answer
np.random.seed(2017)

#FIXME read n from command line
import argparse

#TODO: make code PEP8 compliant
#TODO: make pylint happy, it should have a positive score
#TODO: put calculations into functions

import os

n='10000'

x= np.float32(np.random.uniform(size=10000 ))
y =np.float32(np.random.uniform(size=10000))

a = np.sqrt((x**2)+(y*y))
#count how many points are in the circle, they will be in the circle if x^2 + y^2 is less than 1.0
FILTERED= np.where(a<=1.0)
c =len(a[FILTERED]) #get how many points we just found inside the circle

print("pi is %f" % (4.0 *(c/float(10000))), "from ",n," samples" )
sys.exit(1)
