#!/usr/bin/python
import Tkinter 
from classes import * 
import numpy as np

window_height=1000
window_width=1000

window = Tkinter.Tk() 
window.title("MetroBulider_comeback")
window.geometry(str(window_width) + 'x' + str(window_height)) #window size
canvas = Tkinter.Canvas(window, width=window_width, height=window_height, borderwidth=1, highlightthickness=0, bg="blue")


def draw_circle(circle, **kwargs):
    x = circle.complex.real
    y = circle.complex.imag 
    r = circle.diam/2
    return canvas.create_oval(x-r, y-r, x+r, y+r, **kwargs)

def draw_city(city):
    for i in city.Circles:
        print(i)
        draw_circle(i, fill="red")

c1=Circle(300,200,-200)
c2=Circle(200,200,400)
draw_city(c1)




np.interp(a, (a.min(), a.max()), (-1, +1))







canvas.pack()
window.mainloop()