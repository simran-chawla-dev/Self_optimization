# Contain your back-end logic and classes here
import numpy as np
import pandas as pd
import math

# Instead of coding our math into the front end, we code it into the logic script
# This increases usability of this logic code, and decreases complexity of our GUI objects
def calculate_distance(pt1= (1,1,1), pt2=(2,2,2)):
    '''Calculates the distance between a set of 2 points, (x1,y1,z1) and (x2, y2, z2)'''
    d = math.sqrt((pt2[0]-pt1[0])**2 +(pt2[1]-pt1[1])**2 + (pt2[2]-pt1[2])**2)
    
    return d