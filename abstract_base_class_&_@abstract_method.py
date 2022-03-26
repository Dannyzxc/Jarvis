# abstract_base_class_&_@abstract_method
from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class rectangle(shape):
    type = 'rectangle'
    sides = 4
    def __init__(self):
        self.length = 6
        self.breath = 10

    def print_area(self):
        return self.length * self.breath


rect_01 = rectangle()
print(rect_01.print_area())




