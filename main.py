import random
import time
import turtle
import winsound

winsound.PlaySound('play.wav', winsound.SND_ASYNC)

screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Car game")
screen.tracer(0)
screen.setup(height=600,width=500)
screen.register_shape("car.gif")
screen.register_shape("enemy.gif")

FONT = ("Verdana", 15, "normal")
LİNE_CORD = list()

def path_center_line(x, y):
    centerline = turtle.Turtle()
    centerline.color("white")
    centerline.penup()
    centerline.shape("square")
    centerline.shapesize(0.3, 3)
    centerline.left(90)
    centerline.speed(0)
    centerline.goto(x, y)


for i in range(-300, 400, 100):
    LİNE_CORD.append(i)
for i in LİNE_CORD:
    path_center_line(-120, i)
    path_center_line(117.5, i)


def line(x, y):
    line = turtle.Turtle()
    line.shape("square")
    line.color("black")
    line.penup()
    line.left(90)
    line.shapesize(0.3, 30)
    line.speed(0)
    line.goto(x, y)


line(0, -30)
line(235, 0)
line(-240, 0)

Score = 0
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(0, 270)
score.write(arg=f"Score:0", align="center", font=FONT)

car = turtle.Turtle()
car.shape("car.gif")
car.penup()
car.goto(0, -200)
car.speed(0)


# car.hideturtle()

def right():
    x = car.xcor()
    x += 15
    car.setx(x)


def left():
    x = car.xcor()
    x -= 15
    car.setx(x)


screen.listen()
screen.onkeypress(right, "d")
screen.onkeypress(left, "a")
screen.onkeypress(right, "D")
screen.onkeypress(left, "A")

enemys = []
for i in range(10):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape('enemy.gif')
    enemy.shapesize(2, 4)
    enemy.color('red')
    enemy.setheading(90)
    enemy.penup()
    enemy.dx = random.randint(-170, 170)
    enemy.dy = 500
    enemy.goto(enemy.dx, enemy.dy)
    enemys.append(enemy)

start_time = time.time()
start_time2 = time.time()

i = -1
a = -1
while True:

    if time.time() - start_time2 > random.randint(1, 3):
        start_time2 = time.time()
        i = i + 1
        if i == 9:
            i = -1
            for enemy in enemys:
                enemy.dx = random.randint(-170, 170)
                enemy.dy = 500
                enemy.goto(enemy.dx, enemy.dy)
    y = enemys[i].ycor()
    y = y - 2
    enemys[i].sety(y)

    times = time.time() - start_time
    score.clear()
    score.write(arg=f"Score:{times:.0f}", align="center", font=FONT)
    if enemys[i].distance(car) < 50:
        gameover = turtle.Turtle()
        gameover.color("red")
        gameover.hideturtle()
        gameover.penup()
        gameover.goto(0, 0)
        gameover.write(arg=f"GAME OVER \n   Score: {times:.0f}  ", align="center",
                       font=("Verdana", 25, "bold"))
        score.clear()
        score.write(arg=f"Score: 0", align="center", font=FONT)
        car.goto(0,-200)
        break

    screen.update()


screen.mainloop()