import random
import turtle

screen=turtle.Screen()
screen.bgcolor("blue")
screen.title("Catch The Turtle Game")
score =  0
high_score_file = "highscore.txt"
game_over=False
#turtle list
turtle_list = []
#score turtle
score_turtle = turtle.Turtle()
#countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():
    # score turtle
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()

    # height

    top_height = screen.window_height() / 2
    y = top_height * 0.8

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", font=("Arial", 25, "normal",), align="center")
    score_turtle.pendown()

def make_turtle(x,y):
    #making turtle

    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score:{}".format(score), move=False, font=("Arial", 25, "normal",), align="center")



    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * 10 ,y * 10)
    turtle_list.append(t)
x_cordinates=[20,10,0,-10,-20]
y_cordinates=[-20,-10,0,10,20]
def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x,y)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def show_turtles():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles, 250)
def setup_countdown_turtle(time):
    # countdown turtle
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()

    # height

    top_height = screen.window_height() / 2
    y = top_height * 0.65

    countdown_turtle.setposition(0, y)
    countdown_turtle.pendown()
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, font=("Arial", 25, "normal",), align="center")
        screen.ontimer(lambda: setup_countdown_turtle(time-1),1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game is Finished!", move=False, font=("Arial", 25, "normal",), align="center")
def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles()
    setup_countdown_turtle(10)
    turtle.tracer(1)
start_game_up()
turtle.mainloop()