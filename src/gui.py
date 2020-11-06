# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:10:26 2020

@author: abbme
"""

from tkinter import *
from Coord import *
import jarvis as j
import brute as b
import random


    
points = []
lines = []
canvas = None
frame = None



def callback(event):
    x, y = event.x, event.y
    points.append(Point(x, y))
    canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")
 
# Clears everything
def clear_canvas(e):
    canvas.delete("all")
    points.clear()
    lines.clear()

# Clears lines from the gui so we can try other algorithms
def clear_lines(e):
    canvas.delete("line")
    lines.clear()

# Generates 100 random points for each button click
def random_points(e):
    randomx = []
    randomy = []
    for i in range(0, 100):
        # any random numbers from 0 to 1000
        randomx.append(random.randint(100,900))
        randomy.append(random.randint(100,500))
        x,y = randomx[i], randomy[i]
        points.append(Point(x, y))
        canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")

# Brute force method for convex hull    
def brute(e):
    if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")
    h1,h2 = b.convex_hull(points, len(points))
    n = len(h1)
    for i in range(n):
        canvas.create_line(points[h1[i]].x, points[h1[i]].y, points[h2[i]].x, points[h2[i]].y, tag ="line")

# Jarvis method of convex hull    
def jarvis(e):
    if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")   
    hull = j.convex_hull(points, len(points))
    # Created two more list to improve readability
    hx = []
    hy = []
    for each in hull:
        hx.append(points[each].x)
        hy.append(points[each].y)
    n = len(hx)
    for i in range(n):
        canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line")

# To be used when we implement the preprossesing step of creating
# convex quadrilateral and deleting points within. Not done yet
def del_points(e):
     if display_error() == "er":
        clear_canvas(e)
        raise Exception("Error")

# To be used for the divide and conquer method of convex hull. Not done yet
def sort_points(e):
    quicksort(points,0,len(points)-1)

# display error if less than 3 points
def display_error():
   if (len(points)<3):
        MsgBox = messagebox.showerror("Error", "Put atleast 3 points")
        return "er"

# Display coordinates of all the points being used
def display_points(e):
    for each in points:
        print(each)

        
frame = Frame(None, bg='grey', height=2)
frame.pack()

canvas = Canvas(frame, width="1000", height="600")
canvas.pack(fill=BOTH, expand=1)
canvas.bind('<Button-1>', callback)

pbutton = Button(frame, text="Gen-points")
pbutton.pack(side='left', padx=10)
pbutton.bind('<Button-1>', random_points)

sbutton = Button(frame, text="sort_points")
sbutton.pack(side='left', padx=10)
sbutton.bind('<Button-1>', sort_points)

bbutton = Button(frame, text="Brute")
bbutton.pack(side='left', padx=10)
bbutton.bind('<Button-1>', brute)

jbutton = Button(frame, text="Jarvis")
jbutton.pack(side='left', padx=10)
jbutton.bind('<Button-1>', jarvis)

clearlines = Button(frame, text = "c-lines")
clearlines.pack(side = 'left', padx=10)
clearlines.bind('<Button-1>', clear_lines)

clear = Button(frame, text="clear")
clear.pack(side='left', padx=10)
clear.bind('<Button-1>', clear_canvas)

dbutton = Button(frame, text="display_points")
dbutton.pack(side='left', padx=10)
dbutton.bind('<Button-1>', display_points)

frame.mainloop()


