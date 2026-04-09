from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


point = Point(2, 3)
print(point)
