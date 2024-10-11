# Насута Кирилл ИУ7-12Б. Вариант 4, 3. Решение системы уравнений. Проверка принадлежности точки области. Лабораторная работа №2 Часть 1.

from math import log10
print

# Ввод данных
def initial_data():
    print("\nЗадание 1:")
    print("Введите х:")
    x1 = float(input())

    print("\nЗадание 2:")
    print("Введите х:")
    x2 = float(input())
    print("Введите y:")
    y2 = float(input())

    print("\nЗадание 3:")
    print("Введите х:")
    x3 = float(input())
    print("Введите y:")
    y3 = float(input())

    return x1, x2, y2, x3, y3


def initial_data_task3():
    print("Задание 3:")
    print("Введите х:")
    x3 = float(input())
    print("Введите y:")
    y3 = float(input())

    return x3, y3


# Решение системы уравнений.
def task_1(x):
    if x <= -5:
        y = -x - 5
    else:
        if x <= 0:
            y = x + 5
        else:
            if x < 5:
                y = (25 - x ** 2) ** 0.5
            else:
                y = log10(x - 4)
    return y


# Проверка принадлежности точки функции.
def task_2(x, y):
    if x >= -2.5 and x <= 2.5:
        if y >= 2.5:
            if y <= (9 - x ** 2) ** 0.5 + 3:
                return True
        else:
            if abs(x) >= 2 and abs(x) <= 3:
                if y >= x ** 2 - 6:
                    return True
            else:
                if x >= -2 and x <= 0:
                    if y >= x:
                        return True
                else:
                    if x >= 0 and x <= 2:
                        if y >= -x:
                            return True
    return False


# Проверка принадлежности точки "бабочке"
def task_3(x, y):
    x = abs(x)

    if (x >= 8 and x <= 9):
        if (y >= 7 * (x - 8) ** 2 + 1) and (y <= -0.125 * (x - 9) ** 2 + 8):
            return True
    elif (x > 2 and x < 8):
        if (y >= 1 / 3 * (x - 5) ** 2 - 7 and y <= -0.0625 * x ** 2) or (
                y >= 1 / 49 * (x - 1) ** 2 and y <= -0.125 * (x - 9) ** 2 + 8):
            return True
    elif (x >= 1 and x <= 2):
        if (y >= -2 * (x - 1) ** 2 - 2 and y <= -0.0625 * x ** 2) or (
                y >= 1 / 49 * (x - 1) ** 2 and y <= -0.125 * (x - 9) ** 2 + 8) or (y == 1.5 * x + 2):
            return True
    elif (x <= 1):
        if (y >= 4 * x ** 2 - 6 and y <= -4 * x ** 2 + 2) or (y == 1.5 * x + 2):
            return True

    return False


# Вывод
def output():
    x1, x2, y2, x3, y3 = initial_data()

    print("\nЗадание 1:")
    print(f"{format(task_1(x1), 'g')}")

    print("\nЗадание 2:")
    if task_2(x2, y2):
        print("Точка находится внутри области")
    else:
        print("Точка находится вне области")

    print("\nЗадание 3:")
    if task_3(x3, y3):
        print("Точка находится внутри области")
    else:
        print("Точка находится вне области")


def output_task3():
    x3, y3 = initial_data_task3()
    print("Задание 3:")
    if task_3(x3, y3):
        print("Точка находится внутри области")
    else:
        print("Точка находится вне области")


output_task3()
