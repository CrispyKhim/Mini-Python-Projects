from letter import *

controller = Screen()
score = 0

def showScore():
  global score
  return "You've destroyed " + str(score) + " letters!"

def createController(letterRain):
  controller.bgcolor(0,0,0)
  
  for letter in alphabet:
    controller.onkey(generatePressed(letter, letterRain), letter)
  controller.listen()
  
def pressed(key, letterRain):
  global score
  indices = range(len(letterRain))
  indices.reverse()
  for i in indices:
    letter = letterRain[i]
    if letter.letter == key:
      score += 1
      letter.explode()
      del letterRain[i]
      letterRain.append(fallingLetter())
      
def generatePressed(key, letterRain):
  return lambda : pressed(key, letterRain)
  