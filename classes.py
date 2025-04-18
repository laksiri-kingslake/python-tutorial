class Point:
    default_color = 'red'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing point at ({self.x}, {self.y})")

Point.default_color = 'blue'

point = Point(1, 2)
print(f"Default color: {Point.default_color}")
print(f"Point color: {point.default_color}")

point.default_color = 'green'
print(f"Point color after change: {point.default_color}")
print(f"Default color after point change: {Point.default_color}")

another = Point(3, 4)
print(f"Another point color: {another.default_color}")

point.draw()
another.draw()
