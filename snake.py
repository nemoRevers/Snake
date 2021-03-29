from snakeClass import Snake
import window
from time import sleep

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
    window.closeWindow()
