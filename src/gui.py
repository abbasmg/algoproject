# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:10:26 2020

@author: abbme
"""

from tkinter import *
from jarvis import *

points = []
lines = []
canvas = None
frame = None


def callback(event):
    x = event.x
    y = event.y
    points.append(Point(x, y))
    canvas.create_rectangle(x-1, y-1, x + 1, y + 1, fill="#6F0D5F")
    
def clear_canvas(e):
    canvas.delete("all")
    points.clear()
    lines.clear()
    
def jarvis(e):
    hx,hy = convexHull(points, len(points))
    for i in range(len(hx)-1): 
        canvas.create_line(hx[i], hy[i], hx[i+1], hy[i+1])
    canvas.create_line(hx[-1], hy[-1], hx[0], hy[0])
    
frame = Frame(None, bg='grey', height=2)
frame.pack()

canvas = Canvas(frame, width="600", height="600")
canvas.pack(fill=BOTH, expand=1)
canvas.bind('<Button-1>', callback)

button = Button(frame, text="Jarvis")
button.bind('<Button-1>', jarvis)
button.pack(side='left', padx=10)

clear = Button(frame, text="clear")
clear.pack(side='left', padx=10)
clear.bind('<Button-1>', clear_canvas)

frame.mainloop()


