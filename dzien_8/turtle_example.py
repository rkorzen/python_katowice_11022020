import turtle

turtle.speed(10)

def fill(dist=10, stopDown=False):
    for i in range(dist):
        go_down(dist)
        go_right(1)
        go_up(dist)
        go_right(1)



def go_up(dist):
    turtle.setheading(90)  # north
    turtle.forward(dist)


def go_left(dist):
    turtle.setheading(180)  # west
    turtle.forward(dist)

def go_right(dist):
    turtle.setheading(0)  # east
    turtle.forward(dist)

def go_down(dist):
    turtle.setheading(270)  # south
    turtle.forward(dist)

def even(dist):
    # 10 w prawo
    go_right(20)
    # 10 w dół
    go_down(20)
    # 10 w lewo
    go_left(20)
    # 10 w góre
    go_up(20)
    # na koniec
    go_right(20)

for i in range(10):
    if i % 2 == 0:
        even(20)
    else:
        fill(20)

turtle.done()
