from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: int


student = Student('Jane', 11)
print(student)
