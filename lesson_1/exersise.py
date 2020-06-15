# 1)Создать список из N элементов (от 0 до n с шагом 1).
# В этом списке вывести все четные значения.
#
# 2) СОздать словарь Страна:Столица. Создать список стран.
# Не все страны со списка должны сходиться с названиями стран со словаря.
# С помощою оператора in проверить на вхождение элемента страны в словарь,
# и если такой ключ действительно существует вывести столицу.
#
# 3)Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратных пяти — слово Buzz. Если число кратно пятнадцати,
# то программа должна выводить слово FizzBuzz.
#
# 4) Реализовать функцию bank, которая приннимает следующие аргументы:
# сумма депозита, кол-во лет, и процент. Результатом выполнения должна быть
# сумма по истечению депозита

# 1) ##########################################################################
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in n:
    if i % 2 == 0:
        print(i)

# 2) ##########################################################################
list_of_countries = ['ukraine', 'moldova', 'belorus', 'slovakia', 'usa']
dictionary_of_countries = {
    'ukraine': 'kyiv',
    'usa': 'washington',
    'germany': 'berlin',
    'italy': 'roma'
}

for country in list_of_countries:
    if dictionary_of_countries.get(country):
        print(dictionary_of_countries.get(country))
    else:
        continue

# 3) ##########################################################################
for i in range(100):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    else:
        print(i)

# 4) ##########################################################################


def bank(money, years, percent):
    for i in range(years):
        money = money+(money*percent/100)
    return money


print(bank(100, 10, 5))
