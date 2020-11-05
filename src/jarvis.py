# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:44:01 2020

@author: abbme
"""

# Input x and y is attribute of Point object
# Returns two lists containing both the x and y coordinates of the hull
import time
from Coord import Point

def Leftmost(points,n): 
    # Returns index of the first leftmost point in points list
    minx = points[0].x
    minind = 0
    for i in range(n):
        if minx > points[i].x:
            minx = points[i].x
            minind = i
    return minind
    
def ConvexHull(points,n):
    # Generate convex hull using jarvis algorithm
    tic = time.perf_counter()
    hull = []
    l = Leftmost(points, n)
    first = l
    while(True):
        hull.append(l)
        # Select the point after l in the list
        r = (l + 1)%n
        for i in range(n):
            # Check if points l->i->r turn right and if they do
            # make i the new leftmost point
            if Point.direction(points,l,i,r) < 0:
                r = i
        # The new leftmost point is added to the hull
        l = r
        # if the leftmost point is same as the first point in hull, break from loop
        if l == first:
            break
    toc = time.perf_counter()
    print("Processing time for Brute Force convex hull: " + str(toc-tic) + " seconds")
    return hull
        
    
# points = [] 



# h = ConvexHull(points, len(points))

# for i in h:
#     print(points[i].x,points[i].y)

# points.append(Point(0, 0)) 
# points.append(Point(7, 0)) 
# points.append(Point(3, 3)) 
# direction(0,1,2)
# print(points[Leftmost(points,len(points))].y)  

