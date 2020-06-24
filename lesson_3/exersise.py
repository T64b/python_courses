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


@repeat(30)
def get_sum(number_of_elements):
    summary = []
    for i in range(number_of_elements):
        summary.append(random.randint(0, 1000))
    return summary, sum(summary)


get_sum(5)
