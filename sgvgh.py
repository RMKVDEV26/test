import turtle
window = turtle.Screen()
tom = turtle.Turtle()
n = int(turtle.textinput("PolyMaker","Enter a number"))

if n<3:
    tom.write("Cannot create polygon")
else:
    for i in range(n):
        tom.forward(60)
        tom.left(360/n)
        
window.exitonclick()