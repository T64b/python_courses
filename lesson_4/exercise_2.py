# Создать подобие социальной сети. Описать классы, которые должны
# выполнять соответствующие функции (Предлагаю насследовать класс
# авторизации от класса регистрации). Добавить проверку на валидность
# пароля (содержание символов и цифр), проверка на уникальность логина
# пользователя. Человек заходит, и имеет возможность зарегистрироваться
# (ввод логин, пароль, потдверждение пароля), далее входит в свою учетную
# запись. Добавить возможность выхода из учетной записи, и вход в новый
# аккаунт. Создать класс User, котоырй должен разделять роли обычного
# пользователя и администратора. При входе под обычным пользователем мы
# можем добавить новый пост, с определённым содержимим, так же пост
# должен содержать дату публикации. Под учётной записью администратора
# мы можем увидеть всех пользователей нашей системы, дату их регистрации,
# и их посты.
import datetime
import re

reg_users = []
auth_users = []


def validate_pass(password):
    if len(password) < 8:
        print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]', password) is None:
        print("Make sure your password has a number in it")
    elif re.search('[A-Z]', password) is None:
        print("Make sure your password has a capital letter in it")
    else:
        print("Your password seems fine")
        return True


def find_login(login):
    for user in reg_users:
        if user.login == login:
            return True

    return False


def check_login():
    while True:
        print('Register user')
        log_in = input('Enter log in: ')
        secret = input('Enter pass: ')
        confirm_pass = input('Confirm pass: ')
        if find_login(log_in):
            print('This log in is used, please try again')
            continue
        if not validate_pass(secret):
            print('Not valid password, please try again')
        else:
            return log_in, secret, confirm_pass


def logging_in(user_list, login, password):
    for user in user_list:
        if user.login == login and user.password == password:
            print("You logged in!")
            return user
    return print("Log in or password incorrect ")


def authorization(login, password):
    auth = Authorization(login, password)
    user = auth.login()

    while True:
        text = input('If you want to log out print "logout" ')
        if text == 'logout':
            auth.logout()
            break
        else:
            if user.is_admin:
                user.inspect_users()
            else:
                user.create_post()


class Registration:

    def __init__(self, login, password):
        self._login = login
        self._pass = password

    def register_user(self, admin=False):
        reg_date = datetime.datetime.now()
        user = User(login, password, reg_date, admin)
        reg_users.append(user)


class User:
    is_authorized = False
    is_admin = False

    def __init__(self, login, password, reg_date, admin):
        self._login = login
        self._pass = password
        self.is_admin = admin
        self._reg_date = reg_date
        self._posts = []

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._pass

    def set_login(self, login):
        self._login = login

    def create_post(self):
        if self.is_authorized and not self.is_admin:
            value = input('Enter some text')
            self._posts.append({'date': datetime.datetime.now(), 'post': value})
            print(text)

    def inspect_users(self):
        if self.is_authorized and self.is_admin:
            while True:
                command = input('Enter command "show all" or "exit"')
                if command == 'show all':
                    for user in reg_users:
                        if not user.is_admin:
                            print(user.login, user)
                    continue

                if command == 'exit':
                    break

    def __str__(self):
        posts = ''
        if not self.is_admin:
            for p in self._posts:
                posts += f'date: {p["date"]}, post: {p["post"]} \n'
            return posts
        else:
            return f'{self.login} is admin'


class Authorization(Registration):
    auth_user = None

    def login(self):
        self.auth_user = logging_in(reg_users, self._login, self._pass)
        self.auth_user.is_authorized = True
        auth_users.append(self.auth_user)
        return self.auth_user

    @property
    def logged_user(self):
        return self.auth_user

    def logout(self):
        login_name = self.auth_user.login

        for user in reg_users:
            if user.login == login_name:
                self.auth_user.is_authorized = False
                index = reg_users.index(user)
                reg_users[index] = self.auth_user
                self.auth_user = None
                print(f'User {login_name} logged out')
                break


if __name__ == '__main__':
    reg_users = [User('user1', 'password1', '123131', False),
                 User('user2', 'password2', '123131', False),
                 User('admin', 'password', '123131', True)]
    while True:
        command = input('enter command (auth, reg)')

        if command == 'reg':
            login, password, conf_pass = check_login()

            if password == conf_pass:
                text = input('Do you want to be admin (y/n)')
                is_admin = True if text == 'y' else False
                user = Registration(login, password)
                user.register_user(admin=is_admin)

        if command == 'auth':
            print('Auth user')
            login = input('Enter log in: ')
            password = input('Enter pass: ')
            authorization(login, password)
