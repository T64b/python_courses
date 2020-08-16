# 2) Создать функцию, которая будет скачивать файл из интернета по
# ссылке, повесить на неё созданный декоратор. Создать список из 10
# ссылок, по которым будет происходить скачивание. Создать список
# потоков, отдельный поток, на каждую из ссылок. Каждый поток
# должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание
# закончится.
from threading import Thread
import requests

URLS = ['https://static.videezy.com/system/resources/previews/000/010/283'
        '/original/4k0309.mp4',
        'https://www.facebook.com/favicon.ico',
        'https://i8.rozetka.ua/goods/17468403/xiaomi_l55m5_5aru_images_17468403985.jpg',
        'https://static.testrail.io/6.3.1.1004/images/layout/testrail-logo.svg',
        'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png',
        'https://upst.fwdcdn.com/temp/holidays/8793/logo_ua.gif', ]


def thread(name, daemon):
    def decorator(*func):
        def wrapper(*args):
            threads = []
            for foo in func:
                threads = [Thread(target=foo, args=args, name=name, daemon=daemon)]
            for t in threads:
                t.start()
                print(f'thread {args[1]} started')
        return wrapper

    return decorator


@thread('uploading files', False)
def get_file_by_url(link, name):
    r = requests.get(link, allow_redirects=True)
    open(name, 'wb').write(r.content)
    print(f'thread {name} finished')


for url in URLS:
    name = url.split('/')
    get_file_by_url(url, name[len(name)-1])

