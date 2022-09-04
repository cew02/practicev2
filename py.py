# Code for that special someone in your life :)

name = input("What is your name?")
print("I love you, " + name + ".")

import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):

        pen.right(1)
        pen.forward(1)

def heart():

    pen.fillcolor('red')


    pen.left(140)
    pen.forward(113)

    curve()
    pen.left(120)

    curve()

    pen.forward(112)

    pen.end_fill()

def txt():

    pen.up()

    pen.setpos(-68, 95)

    pen.down()


    pen.color('orange')

# change to whatever name you want and also whatever font and all :)
    pen.write("Love you, ", font=("Verdana", 12, "bold"))


heart()

txt()

pen.ht()