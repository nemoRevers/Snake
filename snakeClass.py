from turtle import Turtle
from window import update
from time import sleep


class Snake:

    def __init__(self, color='green', form='square'):
        self.paramsOfSnake = {'color': color,
                              'form': form}

    body = []

    def addSegment(self, width, height):
        segm = Turtle(self.paramsOfSnake['form'])
        segm.penup()
        segm.color(self.paramsOfSnake['color'])
        segm.goto(width, height)
        self.body.append(segm)

    def move(self, route):
        x = int(self.body[0].position()[0])
        y = int(self.body[0].position()[1])
        self.segment = self.body[-1]
        del self.body[-1]
        self.penultimateSegment = self.body[-1]
        # set coordinates of  first block as end block
        self.segment.goto(x, y)
        self.__route__(route)
        self.body.insert(0, self.segment)
        sleep(1)
        update()

    # turn end block and move forward
    route = 0

    def __route__(self, route):
        if route == "left":
            self.route += 90
            self.penultimateSegment.seth(self.route)
            self.segment.seth(self.route)
            self.segment.forward(20)
        elif route == "right":
            self.route -= 90
            self.penultimateSegment.seth(self.route)
            self.segment.seth(self.route)
            self.segment.forward(20)
