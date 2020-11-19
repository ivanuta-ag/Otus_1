import math


class Figure:
    def __init__(self, name, angles, sideA, sideB):
        self.name = name
        self.angles = angles
        self.sideA = sideA
        self.sideB = sideB

    @property
    def area(self):
        if self.name == 'square':
            return self.sideA ** 2
        elif self.name == 'rectangle':
            return self.sideA * self.sideB
        elif self.name == 'triangle':
            return (self.sideA * self.sideB) / 2
        elif self.name == 'circle':
            return math.pi * (self.sideA ** 2)
        else:
            print('Передана некорректная фигура')

    @property
    def perimeter(self):
        if self.name == 'square':
            return self.sideA * 4
        elif self.name == 'rectangle':
            return (self.sideA + self.sideB) * 2
        elif self.name == 'triangle':
            sideC = math.sqrt(self.sideA ** 2 + self.sideB ** 2)
            return self.sideA + self.sideB + sideC
        elif self.name == 'circle':
            return 2 * math.pi * self.sideA
        else:
            print('Передана некорректная фигура')

    def add_area(self, obj):
        if not isinstance(obj, Figure):
            raise Exception('Передан неправильный класс')
        else:
            return obj.area + self.area
