import time
import colorama
from functools import wraps, singledispatch

colorama.init(autoreset=True)


def sily_decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapper


def timeit(func):  # время выполнения функции
    @wraps(func)  # декоратор для правильного отображения документации и имени функции
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        tac = time.perf_counter()
        elapsed_time = tac - tic
        print(colorama.Fore.MAGENTA + f'время выполнения: {round(elapsed_time, 4)} секунд')
        return value

    return wrapper


def logger(func):  # показывает, какая функция сейчас работает
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'сейчас работает функция {func.__name__}')
        value = func(*args, **kwargs)
        print(f'функция {func.__name__} завершила свою работу')
        return value

    return wrapper


def repeat(rep):  # вызывает нужное количество раз фенкцию
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(rep):
                print(f'{i + 1} повторение')
                func(*args, **kwargs)

        return wrapper

    return decorator


def retry(num_repeat, error_type, sleep_time):  # отлавливает ошибки при работе кода
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_repeat):
                try:
                    return func(*args, **kwargs)
                except error_type:
                    print('верная ошибка отловлена')
                    time.sleep(sleep_time)
                except:
                    print('вышла ошибочка')
                    time.sleep(sleep_time)

        return wrapper

    return decorator


def count_call(func):  # сколько раз вызывают функцию в коде
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        value = func(*args, **kwargs)
        print(f'функция выполнилась {wrapper.counter} раз')
        return value

    wrapper.counter = 0
    return wrapper


def rate_limited(max_per_second):
    """Ограничивает частоту вызова функции"""
    min_interval = 1.0 / float(max_per_second)

    def decorate(function):
        last_time_called = [0.0]

        @wraps(function)
        def rate_limited_function(*args, **kargs):
            elapsed = time.perf_counter() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = function(*args, **kargs)
            last_time_called[0] = time.perf_counter()
            return ret

        return rate_limited_function

    return decorate


@singledispatch  # разные функции вызываютс в зависимости от типа переданных данных
def f(x): return x


@f.register(list)
def _(x): return x


@f.register(int)
def _(x): return x


@count_call
def foo():
    l = []
    for i in range(1_000_000):
        l.append(i)
    return l


foo()
foo()
foo()
