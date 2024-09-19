from math import pi, sqrt
class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=False):
        self.__sides = sides
        self.__color = [*color]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= int(r) <= 255 and 0 <= int(g) <= 255 and 0 <= int(b) <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                if int(i) <= 0:
                    return False
            return True

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

    def __init__(self, color, circumference, filled=True):
        super().__init__([circumference], color, filled)
        self.__radius = circumference / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides, filled=True):
        super().__init__(sides, color, filled)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        area = sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона
        height = (2 * area) / a
        return height

    def get_height(self):
        return self.__height

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # Полупериметр
        return sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь по формуле Герона


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled=True):
        sides = [side_length] * self.sides_count
        super().__init__(sides, color, filled)
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3



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
