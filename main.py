import turtle;

class TurtleDrawing:

    def __init__(self):
        self.screen = turtle.getscreen();
        self.t = turtle.Turtle();
        self.initializeTurtle()
        turtle.Screen().exitonclick();

    def initializeTurtle(self):
        self.t.speed(20)
        previous = 0
        current = 1

        for x in range(20):
            self.square(current)
            self.t.left(90)
            next = current + previous
            previous = current
            current = next

    def square(self, length):
        for i in range(4):
            self.t.forward(length)
            self.t.right(90)
        return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TurtleDrawing()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
