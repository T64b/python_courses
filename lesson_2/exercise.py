# 1) Создать класс автомобиля. Описать общие аттрибуты. Создать
# классы легкового автомобиля и грузового. Описать в основном
# классе базовые аттрибуты для автомобилей. Будет плюсом если в
# классах наследниках переопределите методы базового класса.


class Vehicle:
    def __init__(self, model, color, wheels, max_speed):
        self.model = model
        self.color = color
        self.wheels = wheels
        self.max_speed = max_speed

    def driving(self):
        print('Brrrrrrr-brrrr')

    def beeping(self):
        print('Beeeeeeeeep')

    def travel_time(self, distance):
        return distance / self.max_speed


class Car(Vehicle):
    def beeping(self):
        print('Ring-ring')

    def travel_time(self, distance):
        turbo_boost = 2
        time = distance / (self.max_speed * turbo_boost) * 60
        return time


class Truck(Car):
    weight = 10

    def travel_time(self, distance):
        time = distance / (self.max_speed / self.weight) * 60
        return time


sport_car = Car('Ferrari', 'Red', 4, 300)
big_truck = Truck('Volvo', 'White', 6, 100)
print(big_truck.travel_time(100), 'in minutes')
big_truck.beeping()
print(sport_car.travel_time(100), 'in minutes')


# 2) Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.


class Shop:
    sold_products = 0

    def __init__(self, name, quantity):
        self.name = name
        self.sold_quantity = quantity
        Shop.sold_products += quantity

    def increase_products(self, number):
        Shop.sold_products += number
        self.sold_quantity += number
        return self.sold_quantity

    def show_all_sold_products(self):
        return Shop.sold_products


small_shop = Shop('Levis', 5)
big_shop = Shop('Bershka', 25)

print(big_shop.sold_quantity, '== 25')
print(small_shop.sold_quantity, '== 5')
print(small_shop.show_all_sold_products(), 'all products 25+5')
print(small_shop.increase_products(5))
print(Shop.sold_products)


# Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом
# тип данных.x, y, z). Реалзиовать методы для
# получения и изменения каждой из координат. Перегрузить для этого
# класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, z:{self.z}'

    def __pos__(self):
        x = self.x + 1
        y = self.y + 1
        z = self.z + 1
        return Point(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point(x, y, z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Point(x, y, z)


point = Point(1, 2, 3)
print(point)
point1 = Point(1, 2, 3)
new_point = +point
print(new_point)
