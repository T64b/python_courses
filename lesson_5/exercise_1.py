# 1) Создать декоратор, который будет запускать функцию в отдельном
# потоке. Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.
from threading import Thread


def thread(name, daemon):
    def decorator(func):
        def wrapper(*args):
            print(f'thread {name} started')
            t = Thread(target=func, args=args, name=name, daemon=daemon)
            t.start()
            t.join()
            print(f'thread {t.getName()} finished')
        return wrapper

    return decorator


@thread('Exponentiation', False)
def exponentiation(number, exp):
    print(f'result {number ** exp}')


exponentiation(23424, 23232)

print('Global end')
