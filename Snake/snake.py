"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

writer=Turtle()
colors=["#F8FF33","#BEFF33","#5CFF33","#33FFF1","#3381FF","#5833FF","#DD33FF","#FF33AD","#FF33AD","#F8990B"]
colorB=colors[randrange(0,10)]
colorF=colors[randrange(0,10)]
while colorB == colorF:
    colorF=colors[randrange(0,10)]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food or food in snake:
        print('Snake:', len(snake))
        y=randrange(-15, 15) * 10;
        x=randrange(-15, 15) * 10;
        while vector(x,y)in snake:
            y=randrange(-15, 15) * 10;
            x=randrange(-15, 15) * 10;
        food.x = x
        food.y = y

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorB)

    square(food.x, food.y, 9, colorF)
    update()
    foodMove()
    ontimer(move, 100)
    


def info_alumnos():
    writer.hideturtle()
    writer.up()
    writer.goto(-100,190)
    writer.color("blue")
    writer.write("Carlos Ramos A01197622",align='left')
        
   
def foodMove():
    rNumber = randrange(1,5)
    
    if rNumber == 1 and inside(vector(food.x+10,food.y)):
        food.x = food.x + 10        
    if rNumber == 2 and inside(vector(food.x-10,food.y)):
        food.x = food.x - 10    
    if rNumber == 3 and inside(vector(food.x,food.y+10)):
        food.y = food.y + 10
    if rNumber == 4 and inside(vector(food.x,food.y-10)):
        food.y = food.y - 10     
        

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
info_alumnos()
done()
