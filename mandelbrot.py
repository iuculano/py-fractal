import shutil
import cmath

class Rectangle:    
    def __init__(self, x, y, width, height):
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height


# Use the terminal size as the number of "pixels" on the screen
viewport = shutil.get_terminal_size()

# https://www.bowdoin.edu/~dfrancis/askanerd/mandelbrot/
# Coordinates on the complex plane
#          2i
#          ^
#          |
# -2 <-----------> 2
#          |
#          v 
#         -2i
location = Rectangle(-2.0, 1.5, 0.5, -1.5)

# Distance each "pixel" covers on the defined plane "viewport"
x_step_size = (location.width  - location.x) / viewport.columns
y_step_size = (location.height - location.y) / viewport.lines
cx          = location.x
cy          = location.y

for y in range(viewport.lines):
    for x in range(viewport.columns):
        z = complex(0.0, 0.0)
        c = complex(cx, cy)

        # Great explaination about |z| > 2
        # http://mathforum.org/library/drmath/view/68518.html
        i = 0
        for i in range(512):
            z = (z * z) + c
            
            # When |z| > 2, iterations will continue infinitely
            if abs(z) > 2:
                break

        # Iteration limit (runaway iterations, inside the Mandelbrot set)
        if i == 511:
            print(" ", end = "")

        # Outside the Mandelbrot set
        else:
            print(":", end = "")

        cx += x_step_size

    # The image is created 1 line at a time, thus cx needs to reset at the start
    # of the subsequent line
    cx  = location.x
    cy += y_step_size
    