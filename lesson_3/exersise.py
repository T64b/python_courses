# Создать декоратор с аргументами. Который будет вызывать функцию,
# определенное кол-во раз, будет выводить кол-во времени
# затраченного на выполнение данной функции и её название.
import time
import random


def repeat(repeats):
    def decorator(func):
        def wrapper(number_of_elements):
            for i in range(repeats):
                start_time = time.time()
                print(func(number_of_elements))
                print(f'function name: {func.__name__}, time:'
                      f' {time.time() - start_time} in seconds')

        return wrapper

    return decorator


@repeat(5)
def get_sum(number_of_elements):
    numbers = []
    for i in range(number_of_elements):
        numbers.append(random.randint(0, 1000))
    return numbers, sum(numbers)


get_sum(5)
