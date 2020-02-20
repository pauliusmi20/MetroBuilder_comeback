def _create_circle(self, circle, **kwargs):
    x = circle.complex.real
    y = circle.complex.imag 
    r = circle.diam/2
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

