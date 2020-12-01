#-*- coding: utf-8 -*-
"""
Created on Sun Nov 8 2020
@author: zyadb
"""

"""
pseudocode : Graham scan (wikipedia)
let points be the list of points
let stack = empty_stack()
1. find the lowest y-coordinate and leftmost point, called P0
2. sort points by polar angle with P0, if several points have the same polar angle then only keep the farthest
3. for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
4.    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
5.    push point to stack
end
"""
import time
import math
from math import atan2 # for computing polar angle
from Coord import Point 

"""
# 1. find the lowest y-coordinate and leftmost point, called P0
"""
def lowest_y(points):
    miny = points[0].y
    minind = 0
    for i, point in enumerate(points):
        #print(i,point)
        if point.y < miny:
            miny = point.y
            minind = i
        if point.y == miny:
            if point.x < points[minind].x:
                minind = i

    return points[minind], minind

"""
# 2. sort points by polar angle with P0, if several points have the same polar angle then only keep the farthest
"""
def polar_angle_sort(points,p0):
    sorted_angle = {}
    sorted_index = []
    sorted_points = []
    #calculate the polar angle with p0 for all points
    for i,point in enumerate(points):
        vec_x=point.x-p0.x
        vec_y=point.y-p0.y
        #keeping index to find initial points
        sorted_angle[i] = math.atan2(vec_y, vec_x) 
        #if we find colinear vectors, we calculate lenght and choose farthest
        if sorted_angle.get(i) == sorted_angle.get(i-1):
            d1=math.sqrt(points[i-1].x**2 + points[i-1].y**2)
            d2=math.sqrt(points[i].x**2 + points[i].y**2)
            indice_p1=i-1
            indice_p2=i
            if d1>d2:
                sorted_angle.pop(indice_p2)
            else:
                sorted_angle.pop(indice_p1)

    #sort angles (gives a list)
    sorted_angle=sorted(sorted_angle.items(), key=lambda x: x[1], reverse=False)
    #transform sorted list to dict
    sorted_angle={sorted_angle[i][0]: sorted_angle[i][1] for i in range(0, len(sorted_angle))}
    #get sorted index of points from sorted angle dict
    sorted_index=sorted_angle.keys()
    
    #sort points with sorted index
    for i,index in enumerate(sorted_index):
        sorted_points.append(points[index])
    
    return sorted_points

"""
3. for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
4.    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
5.    push point to stack
end
"""
def convex_hull(points):
    p0,min_id = lowest_y(points)
    points = polar_angle_sort(points,p0)
    convex_hull = []
    convex_ind = []
    
    #P0 and the first point in the sorted list are automatically in the convex hull
    convex_hull.append(p0)
    convex_hull.append(points[1])
    m = 2
    for i in range(2,len(points)):
        while i<len(points):
            direction = convex_hull[m-2].direction(convex_hull[m-1],points[i])
            # print("Iteration:"+str(i-1))
            # print("direction:"+str(direction))
            if direction <= 0:
                #pop stack
                convex_hull.pop()
                m -= 1
            else:
                break
        convex_hull.append(points[i])

        m += 1
        # for j,point in enumerate(convex_hull):
        #     print(point)
        
    return convex_hull  # This needs to be an index of points



# points = []


# points.append(Point(0, 3)) 
# points.append(Point(2, 2)) 
# points.append(Point(1, 1)) 
# points.append(Point(2, 1)) 
# points.append(Point(3, 0)) 
# points.append(Point(0, 0)) 
# points.append(Point(3, 3)) 

# convex_hull(points)



