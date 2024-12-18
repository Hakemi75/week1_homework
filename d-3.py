import math


class Square:
    # コードが期待通り動作するように実装
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def diagonal(self):
        return format(math.sqrt(2) * self.side, ".2f")


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
# print(square2.diagonal())  # 21.21
# print(square2.diagonal())  # 21.21
# print(square2.diagonal())  # 21.21
