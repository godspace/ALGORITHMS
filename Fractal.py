import turtle

bg = turtle.Screen()

player = turtle.Turtle()
player.penup()
player.speed(0)
player.goto(0,-200)
player.left(90)
player.shape('triangle')
player.pendown()

ang = 45

def Tree(size):
  if size > 2:
    player.forward(size)
    player.left(ang)
  
    Tree(size*0.75)
    
    player.right(ang*2)
  
    Tree(size*0.75)
    
    player.left(ang)
    player.forward(-size)

Tree(50)
