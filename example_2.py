import time
import functools

def delay(seconds):
    """
    Декоратор, который задерживает выполнение декорируемой функции на указанное количество секунд.

    :param seconds: Количество секунд задержки.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Ждём {seconds} секунд перед выполнением функции {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример использования декоратора
@delay(2)
def test():
    print('<Тут что-то происходит...>')

@delay(3)
def greet(name):
    print(f'Привет, {name}!')

@delay(1)
def add(a, b):
    return a + b

# Проверка работы декоратора
test()
greet('Алиса')
result = add(3, 5)
print(f'Результат сложения: {result}')
