class player:
  # 1 - constructor - what do I do when I am created
  def __init__(self, playerTurtle):
  # 2 - attributes - what qualities make me unique
    self.turtle = playerTurtle
    
    self.turtle.setx(0)
    self.turtle.sety(0)
    self.turtle.shape("turtle")
    self.turtle.color(0,0,0)
    
    self.jumpSpeed = 6
    self.yVel = 0
    
    self.turtle.penup()
  # 3 - actions - what do I do while I am alive
  def renderPlayer(self, gravity):
    self.yVel += gravity
    
    newYPos = self.turtle.ycor()
    newYPos += self.yVel
    
    self.turtle.sety(newYPos)
  def flap(self):
    self.yVel = self.jumpSpeed