# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:53:30 2020

@author: abbme
"""


class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
 
    def vector(self,p):
        return Point(self.x - p.x, self.y - p.y)        
    
    def direction(points,i, j, k):
        # Returns direction of three points
        # create vectors
        v1 = points[j].vector(points[i])
        v2 = points[k].vector(points[i])        
        # Get cross product of vectors to get direction
        d = v1.x*v2.y - v2.x*v1.y
        # d > 0 : points turn left, d < 0 : points turn right, d = 0 points collinear
        return d