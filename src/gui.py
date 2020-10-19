# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:10:26 2020

@author: abbme
"""

from tkinter import *
import jarvis as j
import brute as b

points = []
lines = []
canvas = None
frame = None

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

def callback(event):
    x, y = event.x, event.y
    points.append(Point(x, y))
    canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")
    
def clear_canvas(e):
    canvas.delete("all")
    points.clear()
    lines.clear()

def clear_lines(e):
    canvas.delete("line")
    lines.clear()
    
def brute(e):
    er = display_error()
    if er == "er":
        clear_canvas(e)
        raise Exception("Error")
    h1,h2 = b.convexHull(points, len(points))
    n = len(h1)
    for i in range(n):
        canvas.create_line(points[h1[i]].x, points[h1[i]].y, points[h2[i]].x, points[h2[i]].y, tag ="line")
    
def jarvis(e):
    er = display_error()
    if er == "er":
        clear_canvas(e)
        raise Exception("Error")        
    hull = j.convexHull(points, len(points))
    # Created two more list to improve readability
    hx = []
    hy = []
    for each in hull:
        hx.append(points[each].x)
        hy.append(points[each].y)
    n = len(hx)
    for i in range(n):
        canvas.create_line(hx[i%n], hy[i%n], hx[(i+1)%n], hy[(i+1)%n], tag ="line")

def display_error():
   if (len(points)<3):
        MsgBox = messagebox.showerror("Error", "Put atleast 3 points")
        return "er"
        
frame = Frame(None, bg='grey', height=2)
frame.pack()

canvas = Canvas(frame, width="600", height="600")
canvas.pack(fill=BOTH, expand=1)
canvas.bind('<Button-1>', callback)

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

frame.mainloop()


