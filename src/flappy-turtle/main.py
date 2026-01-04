from gameStates import *

def init():
  print("Welcome to Flappy Turtle!")
  begin()

def update():
  return runGame()

def end():
  print("Game Over")
  
init()
while True:
  if not update():
    break
end()