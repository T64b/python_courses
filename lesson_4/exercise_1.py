# Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.
from abc import ABC, abstractmethod
from datetime import date


class Person(ABC):
    def __init__(self, last_name, birthday):
        self._last_name = last_name
        self._birthday = birthday

    @property
    def last_name(self):
        return self._last_name

    @property
    def birthday(self):
        return self._birthday

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Enrollee(Person):
    def __init__(self, last_name, birthday, faculty):
        super().__init__(last_name, birthday)
        self._faculty = faculty

    @property
    def faculty(self):
        return self._faculty

    def get_age(self):
        today = date.today()
        day, month, year = self._birthday.split('.')
        return today.year - int(year) - (
                (today.month, today.day) < (int(month), int(day)))

    def __str__(self):
        return f'{self._last_name}, {self._birthday}, {self._faculty}'


class Student(Enrollee):
    def __init__(self, last_name, birthday, faculty, course):
        super().__init__(last_name, birthday, faculty)
        self._faculty = faculty
        self._course = course

    @property
    def course(self):
        return self._course

    def get_age(self):
        today = date.today()
        day, month, year = self._birthday.split('.')
        return today.year - int(year) - (
                (today.month, today.day) < (int(month), int(day)))

    def __str__(self):
        return f'{self._last_name}, {self._birthday}, {self._faculty}, ' \
               f'{self._course}'


class Teacher(Student):
    def __init__(self, last_name, birthday, faculty, course, experience):
        super().__init__(last_name, birthday, faculty, course)
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    def get_age(self):
        today = date.today()
        day, month, year = self._birthday.split('.')
        return today.year - int(year) - (
                (today.month, today.day) < (int(month), int(day)))

    def __str__(self):
        return f'{self._last_name}, {self._birthday}, {self._faculty}, ' \
               f'{self._course}, {self._experience}'


enrollee = Enrollee('Galushkin', '2.05.2010', 'yellow')
student = Student('Petrov', '25.06.1991', 'green', 'programming')
teacher = Teacher('Ivanov', '2.05.1965', 'black', 'economics', '25')

persons = [enrollee, student, teacher]
for i in persons:
    print(i)

info = filter(lambda x: 35 > x.get_age() > 15, persons)

for i in info:
    print(i.last_name, i.get_age())
