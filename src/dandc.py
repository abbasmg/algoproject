# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:54:24 2020

@author: abbme
"""

from Coord import *
import jarvis as j
import brute as b
import math

def divide(points,n,parts):
    points = sort_xy(points,n-1)
    # print("''''''''''''''")
    # for each in points:
    #     print(each)   
    section = n/float(parts)
    if section<3:
        return("Error")
    division = []
    final = 0.0
    while final < n:
        division.append(points[math.floor(final):math.floor(final+section)])
        final = final + section
    return division
    
def convexHull(points,n,parts):
    division = divide(points,n,parts)
    if division == "Error":
        return("Error")
    # cn = len(division)
    # for i in division:
    #     print("part")
    #     for each in i:
    #         print(each)

    hulls = []
    for i in division:
        # print(i)
        hullind = j.convex_hull(i, len(i))
        hull = []
        for h in hullind:
            # print(h)
            # print(i)
            hull.append(i[h])
        hulls.append(hull)
    return(hulls)


# points = [] 
# points.append(Point(0, 3)) 
# points.append(Point(2, 2)) 
# points.append(Point(1, 1)) 
# points.append(Point(2, 1)) 
# points.append(Point(3, 3)) 
# points.append(Point(0, 0)) 
# points.append(Point(3, 0))          




# hulls = convexHull(points,n=len(points),parts=2)

# for i in hulls:
#     print(i)


# len(division)

