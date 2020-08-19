# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.

# пройтись циклом по ключам словаря


class MyList:
    _start = 0

    def __init__(self, *args):
        self._list = list(args)

    @property
    def list(self):
        return self._list

    def append(self, element):
        self._list[len(self._list):] = [element]
        return self._list

    def clear(self):
        self._list = []
        return self._list

    def insert(self, index, element):
        part_1 = self._list[:index]
        part_2 = self._list[index:]
        part_1[len(part_1):] = [element]
        self._list = part_1 + part_2
        return self._list

    def remove(self, element):
        for i in range(len(self._list)):
            if self._list[i] == element:
                part_1 = self._list[:i]
                part_2 = self._list[i+1:]
                self._list = part_1 + part_2
                return self._list
            else:
                continue
        raise ValueError

    def pop(self, element=None):
        if element:
            value = self._list[element]
            part_1 = self._list[:element]
            part_2 = self._list[element + 1:]
            self._list = part_1 + part_2
            return value
        else:
            value = self._list[len(self._list) - 1]
            self._list = self._list[:len(self._list) - 1]
            return value

    def __iter__(self):
        return self

    def __next__(self):
        stop = len(self._list)
        if self._start < stop:
            value = self._list[self._start]
            self._start += 1
            return value
        else:
            raise StopIteration

    def __add__(self, other):
        new_list = self._list + other.list
        return MyList(*new_list)


a = MyList(1, 2)
b = MyList(1, 2)
a.append(3)
a.clear()

a.append(5)
a.append(6)

a.insert(1, 1)
a.insert(1, 2)
a.remove(6)
a.pop(2)
for i in a:
    print(i)
c = a + b
d = c + a
print(list(c))
print(list(d))

# iter_a = iter(a)
# print(next(iter_a))
# print(next(iter_a))
# print(next(iter_a))
