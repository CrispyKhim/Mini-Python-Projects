import turtle, random

screen = turtle.Screen()
screen.bgcolor(192+16,255,192+16)

screen.tracer(0)

a = (0,200)
b = (-200,-200)
c = (200,-200)
triangle = [a,b,c]

turtle.up()
turtle.hideturtle()

prev = (random.uniform(-200,200)), random.uniform(-200,200)

dotCount = 0
dotsPerUpdate = 100

while True:
  turtle.goto(prev)
  dotCount+=1;
  turtle.dot(2,(0,abs(prev[1] + prev[0]),0))
  
  dest = random.choice(triangle)
  prev = (
      (dest[0] + prev[0]) / 2,
      (dest[1] + prev[1]) / 2
    )
  
  if dotCount % dotsPerUpdate == 0:
    screen.update()