import math

# Родительский класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count  # Если количество сторон не совпадает, все стороны равны 1
        else:
            self.__sides = list(sides)  # Иначе сохраняем переданные стороны
        self.filled = False

    # Метод для получения цвета
    def get_color(self):
        return self.__color

    # Проверка корректности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(val, int) and 0 <= val <= 255 for val in [r, g, b])

    # Метод для установки нового цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Проверка корректности сторон
    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    # Метод для получения сторон
    def get_sides(self):
        return self.__sides

    # Метод для изменения сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Периметр фигуры (для круга это длина окружности)
    def __len__(self):
        return sum(self.__sides)

# Класс Circle (наследник Figure)
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)

    # Площадь круга
    def get_square(self):
        return math.pi * (self.__radius ** 2)

# Класс Triangle (наследник Figure)
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Площадь треугольника по формуле Герона
    def get_square(self):
        s = sum(self.get_sides()) / 2  # Полупериметр
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Класс Cube (наследник Figure)
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *([side] * 12))  # Куб имеет 12 рёбер одинаковой длины

    # Объём куба
    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

# Пример использования классов

# Создание круга
circle1 = Circle((200, 200, 100), 10)
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # [55, 66, 77]

# Создание куба
cube1 = Cube((222, 35, 130), 6)
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон
print(cube1.get_sides())  # 12 сторон длиной 6
circle1.set_sides(15)  # Изменится, так как у круга одна сторона
print(circle1.get_sides())  # [15]

# Проверка длины окружности (круг)
print(len(circle1))  # Длина окружности = 15

# Проверка объёма куба
print(cube1.get_volume())  # Объём куба = 6^3 = 216
