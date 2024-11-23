from math import *


# Функция
def func(x):
    y = 2 * x + 52
    return y


# Первообразная
def antiderivative(x):
    y = x ** 2 + 52 * x + 4
    return y


# Обработка ввода
def number_input(name: str, input_type: type):
    while True:
        try:
            number = input_type(input(f"Введите {name}: "))
        except ValueError:
            if input_type == int:
                print("Введенные данные не являются целыми числом")
            else:
                print("Введенные данные не являются числом")
        else:
            break
    return number


# Метод срединных прямоугольников
def medium_rectangles_method(n: int, start: float, end: float):
    integ = 0
    step = (end - start) / n
    curr_x = start
    for i in range(1, n):
        integ += func(curr_x + step / 2)
        curr_x += step
    integ *= step
    return integ


# Метод 3 на 8
def three_and_eight_method(n: int, start: float, end: float):
    integ = func(start) + func(end)
    step = (end - start) / n
    curr_x = start + step
    for i in range(1, n):
        if i % 3 == 0:
            integ += 2 * func(curr_x)
        else:
            integ += 3 * func(curr_x)
        curr_x += step
    integ *= step * 3 / 8
    return integ


# Подсчет точности
def method_inaccuracy(integ: float, start: float, end: float):
    absolute_inaccuracy = integ - (antiderivative(end) - antiderivative(start))
    eps = -1e9
    if antiderivative(end) - antiderivative(start) <= eps:
        return absolute_inaccuracy, absolute_inaccuracy
    relative_inaccuracy = abs(absolute_inaccuracy / (antiderivative(end) - antiderivative(start)))
    return absolute_inaccuracy, relative_inaccuracy


# Проверка возможности форматировать, в перменной type: 0 - обычное форматирвание 1 - форматирование в проценты
def try_format(value, type):
    try:
        if type == 0:
            return format(value, '.5g')
        else:
            return format(value, '5%')
    except:
        return value
