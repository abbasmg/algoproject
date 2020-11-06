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
    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + "\n"


def pivot_partition(points,low,high):
    i = (low)         
    pivot = points[low].x     
    for j in range(high, low, -1):  
        if points[j].x < pivot: 
            for k in range(i,j-1):
                if points[k].x > pivot:
                    i = k
                    break      
            points[i],points[j] = points[j],points[i] 
        # print(i,j)      
        if i >= j:
            points[low],points[j] = points[j],points[low] 
            break
    return (high) 
    

    
def quicksort(points,low,high): 
    if low < high: 
        pi = pivot_partition(points,low,high)   
        quicksort(points, low, pi-1) 
        quicksort(points, pi+1, high) 
    return points
        

# def pivot_partition(points,low,high):
#     pi = low
#     pivot = points[low].x     
#     low = pi + 1    
#     while True:
#         while low <= high and points[high].x >= pivot:
#             high = high - 1
#         while low <= high and points[low].x <= pivot:
#             low = low + 1
#         if low <= high:
#             points[low], points[high] = points[high], points[low]
#         else:
#             break
#     points[pi], points[high] = points[high], points[pi]
#     return high


    
    
# points = []
# points.append(Point(4, 3))
# points.append(Point(0, 9)) 
# points.append(Point(7, 2)) 
# points.append(Point(5, 3))
# points.append(Point(5, 3))
# points.append(Point(3, 3))
# points.append(Point(1, 3))



# # quickSort(points,0,len(points)-1)

# # # pi = pivot_partition(points,0,len(points)-1)

# # print(pi)

# for each in points:
#     print(each)

# len(points)-1
