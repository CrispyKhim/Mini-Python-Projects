from controller import *

letterRain = []

def init():
  createController(letterRain)
  for i in range(5):
    letterRain.append(fallingLetter())
  
def update():
  for letterDrop in letterRain:
    letterDrop.fall()
    if letterDrop.isAtBottom():
      return False
  return True
  
def end():
  print("Game over")
  
init()
while True:
  if not update():
    break;
end()