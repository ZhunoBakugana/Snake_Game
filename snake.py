from turtle import Turtle

STARTING_POSITIONS = [(0,0) ,(-20,0),(-40,0)]
MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for body_part in STARTING_POSITIONS:
           self.add_body_part(body_part)

    def add_body_part(self, body_part):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(body_part)
        self.snake_body.append(snake)

    def extend(self):
        self.add_body_part(self.snake_body[-1].position())

    def remove_parts(self):
        for body_parts in self.snake_body[3:]:
            self.snake_body.remove(body_parts)
            body_parts.reset()
        self.head.teleport(0,0)

    def move(self):
        for snake_spawn in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_spawn - 1].xcor()
            new_y = self.snake_body[snake_spawn - 1].ycor()
            self.snake_body[snake_spawn].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.head.setheading(0)
