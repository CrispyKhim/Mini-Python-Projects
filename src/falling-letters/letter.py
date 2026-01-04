from turtle import Turtle, Screen
import random
from string import ascii_lowercase as alphabet # [a,b,c ... ,y,z]

class fallingLetter:
  # 1. constructor - what do I do when I am created?
  def __init__(self):
    # 2. attributes - what qualities make me unique?
    self.letter = random.choice(alphabet)
    self.isFalling = True
    
    self.turtle = Turtle()
    
    self.turtle.penup()
    self.turtle.setposition(random.randint(-200,200),200)
    self.turtle.hideturtle()
    self.turtle.speed(10)
    self.turtle.setposition(random.randint(-200,200),200)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    self.turtle.color(r,g,b)
    
  # 3. actions - what do I do while I am alive?
  def fall(self):
    if not self.isFalling:
      return
    self.turtle.clear()
    x, y = self.turtle.xcor(), self.turtle.ycor() - 2;
    self.turtle.goto(x, y)
    self.turtle.write(self.letter, align="center", font=("Arial", 20))
    
  def isAtBottom(self):
    return self.turtle.ycor() <= -200
    
  def explode(self):
    self.isFalling = False
    self.turtle.pendown()
    self.turtle.pensize(random.randint(5,30))
    self.turtle.goto(self.turtle.xcor(), 200)