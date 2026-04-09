from enum import Enum


class Direction(Enum):
    NORTH = 'north'
    SOUTH = 'south'
    EAST = 'east'
    WEST = 'west'


for direction in Direction:
    print(direction.name, direction.value)
