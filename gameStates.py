import turtle, random, time
from player import *
from obstacle import *

gameState = None

gravity = -0.2

controller = turtle.Screen()
flappy = player(turtle.Turtle())
barrage = []
timeSync, timeDelay = 0, 1

def runGame():
  if gameState:
    result = gameState()
    controller.update()
    return result
  return True
  
def begin():
  global gameState, flappy, barrage, timeSync
  
  gameState = None
  flappy.turtle.sety(0)
  
  for thisOb in barrage:
    thisOb.turtle.clear()
    thisOb.turtle.hideturtle()
  barrage = []
  timeSync = time.time()
  
  controller.tracer(0)
  controller.onkey(flap, "space")
  controller.listen()
  
  print("Press the Space Bar to begin.")

def game():
  global gameState, barrage, timeSync
  flappy.renderPlayer(gravity)
  yPos = flappy.turtle.ycor()
  if yPos < -200 or yPos > 200:
    gameState = finish
  
  if time.time() >= timeSync:
    barrage.append(obstacle(turtle.Turtle(), random))
    timeSync += timeDelay
  
  for thisOb in barrage:
    thisOb.move()
    if thisOb.isTouching(flappy):
      gameState = finish
    if thisOb.hasReachedEnd():
      thisOb.disappear()
      barrage.remove(thisOb)

  return True

def finish():
  global gameState
  print("You lose")
  
  controller.onkey( begin, "y")
  controller.onkey( doClose, "n")
  controller.listen()
  
  print("Do you want to try again? (y/n)")
  gameState = None
  return True
  
def flap():
  global gameState
  flappy.flap()
  if gameState != game:
    gameState = game

def doClose():
  global gameState
  gameState = close
  
def close():
  return False