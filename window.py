from turtle import Screen


def openWindow():
    global window
    window = Screen()
    window.setup(width=600, height=600)
    window.bgcolor('black')
    window.title('Snake')
    window.tracer(0)


def closeWindow():
    window.exitonclick()


def update():
    window.update()
