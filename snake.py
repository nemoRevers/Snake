import window
from snakeClass import Snake

if __name__ == '__main__':
    window.openWindow()
    snake = Snake('green', 'square')

    for i in [(0, 0), (-20, 0), (-40, 0)]:
        snake.addSegment(i[0], i[1])
    window.update()

    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')
    snake.move('left')

    # TEST

    # turtle1 = Turtle('square')
    # turtle2 = Turtle('square')
    # turtle3 = Turtle('square')
    # turtle3.color('blue')
    # turtle2.goto(-20, 0)
    # turtle2.color('green')
    # turtle1.color('red')
    # turtle1.goto(0, 0)
    # turtle3.goto(-40, 0)
    # window.update()
    # def op():
    #     turtle2.left(90)
    #     turtle3.goto(0, 0)
    #     turtle3.left(90)
    #     turtle3.forward(20)
    #     window.update()
    # op()
    window.closeWindow()
