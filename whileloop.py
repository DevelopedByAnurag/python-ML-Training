import turtle



def square():
    turtle1=turtle.Turtle()
    turtle1.speed(15)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    turtle1.right(90)
    turtle1.forward(100)
    pass

#while loop

player1="happy"
player1Counts=10
while player1 =="happy":
    square()
    print('counts left:',player1Counts)
    if player1Counts <= 0:
        break
    player1Counts-=1
    
    
