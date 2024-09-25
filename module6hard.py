from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides: int):
        self.filled = False
        self.__sides = [*sides]
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        self.__color = [*color]
        if self.set_color(*color):
            if isinstance(self.__color, (int, float)):
                pass
        else:
            self.__color = [0, 0, 0]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return True
        else:
            return False

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                if not isinstance(i, int) or i <= 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__radius = sides[0] / (2 * pi)
        else:
            self.__radius = 0

    def get_square(self):
        return pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.height = self.get_square()

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        area = sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона
        height = (2 * area) / a
        return height

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_sides(*list(sides) * 12)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
