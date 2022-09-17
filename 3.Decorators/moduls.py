from functools import wraps
from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        st = datetime.now().ctime()
        arg = args
        name = func.__name__
        res = func(*args, **kwargs)
        with open('log.txt', 'a', encoding='utf-8') as file_:
            file_.write(f'Имя функции: {name}\nВремя и дата запуска: {st}\nПередаваемые аргументы: {arg}\nВозвращает: {res}\n{"-" * 100}\n')
        return res
    return wrapper

def logger_sign_decorator(file_name):
    def logger_sign(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            st = datetime.now().ctime()
            arg = args
            name = func.__name__
            res = func(*args, **kwargs)
            with open(file_name, 'a', encoding='utf-8') as file_:
                file_.write(
                    f'Имя функции: {name}\nВремя и дата запуска: {st}\nПередаваемые аргументы: {arg}\nВозвращает: {res}\n{"-" * 100}\n')
                return res

        return wrapper
    return logger_sign