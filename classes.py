"""
Learning Python Classes
"""

class Point:
    default_color = 'red'

    def __init__(self, x, y):
        """Initialize the point with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """Return a string representation of the point."""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Check if two points are equal."""
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        """Check if this point is greater than another point."""
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
        """Add two points together."""
        return Point(self.x + other.x, self.y + other.y)
    
    @classmethod
    def zero(cls):
        """Set the point to the origin (0, 0)."""
        return cls(0, 0)

    def draw(self):
        """Draw the point on the screen."""
        # In a real application, this would use a graphics library
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

default_point = Point.zero()
default_point.draw()

print(point)

another = Point(-4, -9)
print(point == another)
print(point > another)
print(point < another)

print(point + another)
