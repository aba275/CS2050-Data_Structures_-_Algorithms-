import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(13)
        tree(branchLen-15,t)
        t.left(26)
        tree(branchLen-15,t)
        t.right(13)
        t.backward(branchLen)
    if branchLen < 20:
        t.color("green")
    else:
        t.color("brown")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()

main()
