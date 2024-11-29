import functools

def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} была вызвана {wrapper.count} раз(а).")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

# Пример использования декоратора
@counter
def test():
    print('<Тут что-то происходит...>')

@counter
def greet(name):
    print(f'Привет, {name}!')

@counter
def add(a, b):
    return a + b

# Проверка работы декоратора
test()
test()
greet('Алиса')
greet('Боб')
result = add(3, 5)
print(f'Результат сложения: {result}')
result = add(10, 20)
print(f'Результат сложения: {result}')
