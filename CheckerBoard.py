def checkers():

    import turtle

    turtle.color('black', 'black')

    turtle.pu()

    turtle.speed(50)

    turtle.goto(-300, 300)

    turtle.pd()
    turtle.begin_fill()
    for i in range (4):
        for i in range (2):
            for i in range (4):
                turtle.begin_fill()
                for i in range (4):
                    turtle.forward(75)
                    turtle.right(90)
                turtle.end_fill()
                turtle.pu()
                turtle.forward(150)
            turtle.right(90)
            turtle.forward(75)
            turtle.right(90)
            turtle.forward(525)
            turtle.right(180)
        turtle.left(180)
        turtle.forward(150)
        turtle.left(180)
    turtle.pd()
    for i in range (4):
        turtle.begin_fill()
        turtle.forward(600)
        turtle.left(90)
        turtle.end_fill()
            
 
