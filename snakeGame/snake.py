from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):


    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        init_pos = [0, -20, -40]  #initial position of its body
        for pos in init_pos:
            snake_part = Turtle("square")
            snake_part.color('white')
            snake_part.penup()
            snake_part.goto(y=0, x=pos)
            self.body.append(snake_part)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.body.append(new_segment)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)

        self.head.fd(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for part in self.body:
            part.goto(1000,1000)
        self.body.clear()
        self.create_body()
        self.head = self.body[0]