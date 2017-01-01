from enum import Enum

class Shape(Enum):
    SQUARE = 2
    DIAMOND = 1
    CIRCLE = 3
    ALIAS_FOR_SQUARE = 2

print(Shape.SQUARE) #Shape.SQUARE