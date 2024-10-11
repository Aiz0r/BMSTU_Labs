# Насута Кирилл ИУ7-12Б. Решение квадратного уравнения. Лабораторная работа №2 Часть 1.

# Уравнение вида: ax^2+bx+c=0.
# Ввод данных
def initial_data():
    print("Введите коэффициент уравнения а:")
    a = float(input())
    print("Введите коэффициент уравнения b:")
    b = float(input())
    print("Введите коэффициент уравнения c:")
    c = float(input())
    return a, b, c


# Реализация алгоритма.
def realization(a, b, c):
    if a != 0:
        D = b ** 2 - 4 * a * c
        if D < 0:
            return ("Уравнение не имеет решений")
        else:
            if D > 0:
                x1 = (-b - D ** 0.5) / (2 * a)
                x2 = (-b + D ** 0.5) / (2 * a)
                return (f"Уравнение имеет два решения:\n x1 = {format(x1, 'g')}\n x2 = {format(x2, 'g')}")
            else:
                x = -b / 2 * a
                return (f"Уравнение имеет одно решение:\n x = {format(x, 'g')}")
    else:
        if b != 0:
            x = -c / b
            return (f"Уравнение имеет одно решение:\n x = {format(x, 'g')}")
        else:
            if c != 0:
                return ("Уравнение не имеет решений")
            else:
                return ("Уравнение имеет бесконечное число решений")


# Вывод.
def output():
    a, b, c = initial_data()
    print(realization(a, b, c))


output()
