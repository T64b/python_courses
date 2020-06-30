# Создать класс структуры данных Стек, Очередь. Создать класс
# комплексного числа и реализовать для него арифметические
# операции.


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def top(self):
        return self._items[len(self._items) - 1]

    def length(self):
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def top(self):
        return self._items[len(self._items) - 1]

    def length(self):
        return len(self._items)


s = Stack()
s.push(1)
s.push('cat')
s.push(3)
print(s.top())
s.pop()
print(s.length())


q = Queue()
q.enqueue(1)
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
print(q.top())
print(q.length())

# ______________________________________________________________________________


class Complex:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def __str__(self):
        if self._imag == 0:
            return f'{self._real}'
        elif self._imag < 0:
            return f'{self._real}{self._imag}i'
        else:
            return f'{self._real}+{self._imag}i'

    def __add__(self, other):
        real = self._real + other.real
        imag = self._imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        real = self._real - other.real
        imag = self._imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self._real * other.real - self._imag * other.imag
        imag = self._imag * other.real + self._real * other.imag
        return Complex(real, imag)

    def __truediv__(self, other):
        real = (self._real * other.real + self._imag * other.imag) / \
               (other.real * other.real + other.imag * other.imag)
        imag = (self._imag * other.real - self._real * other.imag) / \
               (other.real * other.real + other.imag * other.imag)
        return Complex(real, imag)


num1 = Complex(1, 2)
num2 = Complex(2, 4)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
