# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.
# Указанные методы описываем самостоятельно, без использования
# стандартных.


class MyDictionary:
    _start = 0

    def __init__(self, **kwargs):
        self._dict = kwargs
        self._keys = list(kwargs)

    @property
    def dictionary(self):
        return self._dict

    def get(self, key):
        try:
            return self._dict[key]
        except KeyError:
            return None

    def values(self):
        values = []
        for key in self._dict:
            values.append(self._dict[key])
        return values

    def keys(self):
        return self._keys

    def items(self):
        items = []
        for key in self._dict:
            items.append((key, self._dict[key]))
        return items
    #
    # def __iter__(self):
    #     return self._dict

    def __add__(self, other):
        dictionary = {}
        adding = self.items() + other.items()
        for item in adding:
            dictionary.update({item[0]: item[1]})
        return MyDictionary(**dictionary)


d = MyDictionary(a=1, b=2, c=3)
g = MyDictionary(d=1, e=2, f=3)
print(d.keys(), d.values(), d.items())
new_dict = d+g
print(new_dict.dictionary)
print(new_dict.keys())
print(new_dict.values())

