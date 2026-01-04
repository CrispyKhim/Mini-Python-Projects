import turtle, random

score = 0

screen = turtle.Screen()
screen.bgcolor(255,255,192+16)

penny = turtle.Turtle()
penny.shape('circle')
penny.goto(0,0)
penny.up()
penny.speed(0)

def gotoRandom(x,y):
  global score
  score += 1
  print(score)
  penny.goto(
    random.randint(-200,200),
    random.randint(-200,200)
  )

def init(x,y):
  penny.onclick(gotoRandom)
  screen.ontimer(end, 10000)
  
def end():
  penny.hideturtle()
  penny.goto(0,0)
  penny.write(
    "You've clicked Penny" + str(score) + " times.",
    font = (("Courier", 10, 'italic'), 15),
    align = "center"
  )

penny.goto(0,50)
penny.write(
    "You have 10 seconds to click on Penny the dot.",
    font = (("Courier", 10, 'italic'), 10),
    align = "center"
  )
penny.goto(0,20)
penny.write(
    "Click on Penny to start.",
    font = (("Courier", 10, 'italic'), 15),
    align = "center"
  )
penny.goto(0,0)
penny.onclick(init)