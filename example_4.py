import functools

def memoize(func):
    """
    Декоратор, который кэширует результаты вызова функции и возвращает
    сохранённый результат при повторном вызове с теми же аргументами.
    """
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Возвращаем кэшированный результат для аргументов {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print(f"Сохраняем результат для аргументов {args}")
            return result

    return wrapper

# Пример использования декоратора с рекурсивной функцией вычисления чисел Фибоначчи
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Проверка работы декоратора
print(fibonacci(10))  # Вычисление числа Фибоначчи для n=10
print(fibonacci(15))  # Вычисление числа Фибоначчи для n=15
print(fibonacci(10))  # Повторное вычисление числа Фибоначчи для n=10 (должно использовать кэш)
