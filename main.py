from turtle import *
from random import *
import time

class blob:
  # 1 - constructor: what do I do when I am created?
  def __init__(self):
    # 2 - attributes: what qualities make me unique?
    self.turtle = Turtle()
    self.turtle.penup()
    self.turtle.setpos(uniform(-200,200), uniform(-200,200))
    self.turtle.color(0,150,25)
    self.turtle.pencolor(0,255,0)
    self.turtle.speed(uniform(5,30))
    self.turtle.shape('circle')
    
    self.isSquished = False
    
    self.turtle.pendown()
    self.turtle.onclick(self.squish)
    
  # 3 - actions what do I do while I am alive?
  def move(self):
    if self.isSquished:
      return 1
    
    self.turtle.fd(1)
    self.turtle.rt(uniform(-30,30))
    return 0
    
  def bounce(self):
    if abs(self.turtle.xcor()) > 200 or abs(self.turtle.ycor()) > 200:
      self.turtle.rt(180)
      self.move()
  
  def squish(self, mouseX, mouseY):
    self.isSquished = True
    self.turtle.pensize(20)
    self.turtle.color("yellow")
    self.turtle.dot()

blobPile = []
startTime = time.time()
def init():
  Screen().bgcolor(192+20,192+8,192)
  Screen().tracer(0)
  
  for i in range(10):
    blobPile.append( blob() )
  
def update():
  totalSquished = 0
  for thisBlob in blobPile:
    totalSquished += thisBlob.move()
    thisBlob.bounce()
  
  Screen().update()
  
  if totalSquished >= len(blobPile):
    return False
  return True
  
def end():
  timeTaken = time.time() - startTime
  print("You squished all the blobs!")
  print("It took you: " + str(timeTaken) + " seconds.")
  

init()
while True:
  if not update():
    break
end()