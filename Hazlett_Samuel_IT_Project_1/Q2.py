Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
... 
... canvas = turtle.Screen()
... canvas.setup(400, 400, startx=900, starty=-200)
... 
... print("This program can draw different shapes.")
... 
... # Take input from user on what to draw
... shape = input("Type what you want to draw (triangle, square, circle, star): ")
... 
... # Take input from user for drawing color
... drawColor = input("Choose a color (red, green, blue, pink, purple, black, yellow, brown): ")
... 
... # Set drawing color
... turtle.pencolor(drawColor)
... 
... # If user types triangle, draw a triangle
... if shape == "triangle":
...     # The following code draws a triangle
...     for i in range(3):
...         turtle.forward(100)
...         turtle.right(120)
... 
... # If user types square, draw a square
... elif shape == "square":
...     # The following code draws a square
...     for i in range(4):
...         turtle.forward(100)
...         turtle.right(90)
... 
... # If user types circle, draw a circle
... elif shape == "circle":
...     # Code to draw a circle
...     turtle.circle(100)
... 
... # If user types star, draw a star
elif shape == "star":
    # Code to draw a star
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

# If the user input doesn't match any shape
else:
    print("Sorry, I don't know how to draw that shape.")

turtle.done()
