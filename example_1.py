import functools

def how_are_you(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Запрос у пользователя "Как дела?"
        input("Как дела? ")
        # Вывод фиксированного сообщения
        print("А у меня не очень! Ладно, держи свою функцию.")
        # Вызов декорируемой функции с теми же аргументами и ключевыми словами
        return func(*args, **kwargs)
    return wrapper

# Пример использования декоратора
@how_are_you
def test():
    print('<Тут что-то происходит...>')

@how_are_you
def greet(name):
    print(f'Привет, {name}!')

@how_are_you
def add(a, b):
    return a + b

# Проверка работы декоратора
test()
greet('Алиса')
result = add(3, 5)
print(f'Результат сложения: {result}')
