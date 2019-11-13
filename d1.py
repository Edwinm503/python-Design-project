import turtle
bob = turtle.Turtle()
bob.speed(0)
bob.color("blue")
turtle.bgcolor("black")
bob.width(7)  
for times in range(30):
     for times in range(4):
        
      bob.forward(100)
     bob.right(60) 
     bob.forward(100)
     bob.right(120)
     bob.right(36)
     bob.left(60)
     bob.forward(100)
     
bob.width(10)     
bob.color("red")
for times in range(10):
  for times in range(2):
     bob.forward(100)
     bob.right(60)
     bob.forward(100)
     bob.right(120)
  bob.right(36)
