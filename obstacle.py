class obstacle:
  # 1. constructor - what do I do when I am created?
  def __init__(self, turtle, random):
  # 2. attributes - what qualities make me unique?
    self.turtle = turtle
    self.turtle.penup()
    self.turtle.shape("classic")
    self.turtle.goto(200, random.uniform(-200,200))
    
    self.random = random
    self.speed = 1
    
    self.turtle.setheading(180)
    self.turtle.color(255,0,0)
    self.turtle.pendown() # trail
    
  # 3. actions - what do I do while I am alive?
  def move(self):
    self.turtle.fd(self.speed)
    self.turtle.rt(self.random.uniform(-1,1))
  def disappear(self):
    self.turtle.hideturtle()
  def hasReachedEnd(self):
    return self.turtle.xcor() <= -200
  def isTouching(self, player):
    return self.turtle.distance(player.turtle) < 15