import turtle
import random
TRACK_X, TRACK_Y, TRACK_LEN, TRACK_WIDTH, LANE_WIDTH= -350,200,700,400,100
LANE_NUMBER_X, LANE_NUMBER_Y = -380 ,130
FINISH_X = 250
TURTLE_X, TURTLE_Y =-300, 150
def setup_screen():
  global screen,turt
  screen = turtle.getscreen()
  screen.setup(800, 500)
  screen.title("TYM-Racing Turtles")
  screen.bgcolor("#9F4123")
  turt = turtle.getturtle()
  turt.speed(0)
  turt.penup()
  turt.goto(-100, 205)
  turt.color("white")
  turt.write("Racing Turtles", font=("Arial", 20, "bold"))
  draw_track()
  draw_finishline()
  
def draw_track():
  turt.goto(TRACK_X,TRACK_Y)
  turt.color("chocolate")
  turt.pendown()
  turt.begin_fill()
  for x in range (2):
    turt.forward(TRACK_LEN)
    turt.right(90)
    turt.forward(TRACK_WIDTH)
    turt.right(90)
  turt.end_fill()
  for index in range(5):
    turt.color("white")
    turt.penup()
    turt.goto(TRACK_X, TRACK_Y-index * LANE_WIDTH)
    turt.pendown()
    turt.forward(TRACK_LEN)
  turt.penup()
  for index in range(4):
    turt.goto(LANE_NUMBER_X, LANE_NUMBER_Y-index * LANE_WIDTH)
    turt.write(index+1, font = ("Arial",20,"bold"))
def draw_finishline():
  turt.penup()
  turt.goto(FINISH_X, TRACK_Y)
  turt.seth(270)
  turt.pendown()
  turt.begin_fill()
  turt.begin_fill()

  for i in range(2):
    turt.forward(TRACK_WIDTH)
    turt.left(90)
    turt.forward(40)
    turt.left(90)
  turt.end_fill()
  turt.left(90)
  turt.forward(20)
  turt.color("black")
  turt.begin_fill()
  for x in range(10):
    turt.forward(20)
    turt.right(90)
    turt.forward(20)
    turt.right(90)
    turt.forward(40)
    turt.left(90)
    turt.forward(20)
    turt.left(90)
    turt.forward(20)
  turt.left(90)
  turt.forward(400)
  turt.end_fill()
  turt.hideturtle()
def setup_turtles():
  global Battery, Tim, Nathan , Aaron
  Battery = turtle.Turtle()
  Tim = turtle.Turtle()
  Nathan = turtle.Turtle()
  Aaron = turtle.Turtle()
  global turtleList
  turtleList = [Battery, Tim, Nathan, Aaron]
  colourList = ["lightblue", "pink", "red", "green"]
  for i in range(4):
    currTurt = turtleList[i]
    currTurt.penup()
    currTurt.color(colourList[i])
    currTurt.shape("turtle")
    currTurt.turtlesize(2)
    currTurt.goto(TURTLE_X, TURTLE_Y - LANE_WIDTH * i)
    currTurt.pendown()

def get_userguess():
  return screen.numinput("GUESS", "Which turtle will win? (1,2,3,4)", minval = 1, maxval = 4)
def race(user_guess: int):
  while (Battery.xcor() <= FINISH_X and Tim.xcor() <= FINISH_X and Nathan.xcor() <= FINISH_X and Aaron.xcor() <= FINISH_X):
    for pen in turtleList:
      pen.forward(random.randint(1, 20))
  for index in range(4):
    if turtleList[index].xcor() > FINISH_X:
      Winner = index + 1
  if user_guess == Winner:
    screen.textinput("Game over!","You win! Turtle " + str(Winner) + " won the game")
  else:
    screen.textinput("Game over!","You lost! Turtle " + str(Winner) + " won the game")
  
def main():
    setup_screen()
    setup_turtles()
    user_guess = get_userguess()
    race(user_guess)
if __name__ == "__main__":
  main()