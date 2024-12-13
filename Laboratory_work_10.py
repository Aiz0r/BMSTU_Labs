# Насута Кирилл ИУ7-12Б Программа, ищущая интегралы функции методом срединных прямоугольников и 3/8, а также считающая и сравнивающая их погрешность
from Laboratory_work_10_func import *

# Обработка ввода
start = 1
end = 0
while start > end:
    start = number_input("начало отрезка интегрирования", float)
    end = number_input("конец отрезка интегрирования", float)
    if start > end:
        print("Ошибка ввода, число начала отрезка должно быть меньше конца")

N1 = number_input("количество участков разбиения N1", int)
N2 = number_input("количество участков разбиения N2", int)
method_1_1 = medium_rectangles_method(N1, start, end)
method_1_2 = medium_rectangles_method(N2, start, end)
if N1 % 3 != 0:
    method_2_1 = '-'
else:
    method_2_1 = three_and_eight_method(N1, start, end)
if N2 % 3 != 0:
    method_2_2 = '-'
else:
    method_2_2 = three_and_eight_method(N2, start, end)

# Вывод таблиц
print("Таблица вычисленных интегралов \n")
print("-" * 84)
print(
    "| Количество отрезков разбиения / методы " + "|" + f"{try_format(N1, 0): ^20}" + "|" + f"{try_format(N2, 0): ^20}" + "|")
print("-" * 84)
print(
    "| Метод срединных прямоугольников " + " " * 7 + "|" + f"{try_format(method_1_1, 0): ^20}" + "|" + f"{try_format(method_1_2, 0): ^20}" + "|")
print("-" * 84)
print(
    "| Метод 3/8 " + " " * 29 + "|" + f"{try_format(method_2_1, 0): ^20}" + "|" + f"{try_format(method_2_2, 0): ^20}" + "|")
print("-" * 84 + '\n')

# Вывод погрешностей
print("Погрешности метода срединных прямоугольников:")
method_absolute_inaccuracy, method_relative_inaccuracy = method_inaccuracy(method_1_1, start, end)
print(
    f"Абсолютная погрешность при разбиении на {try_format(N1, 0)} участков: {try_format(method_absolute_inaccuracy, 0)}")
print(
    f"Относительная погрешность при разбиении на {try_format(N1, 0)} участков: :  {try_format(method_relative_inaccuracy, 1)}")
print()
method_absolute_inaccuracy, method_relative_inaccuracy = method_inaccuracy(method_1_2, start, end)
print(
    f"Абсолютная погрешность при разбиении на {try_format(N2, 0)} участков: {try_format(method_absolute_inaccuracy, 0)}")
print(
    f"Относительная погрешность при разбиении на {try_format(N2, 0)} участков: {try_format(method_relative_inaccuracy, 1)}")
print()
if method_2_1 != '-':
    method_absolute_inaccuracy, method_relative_inaccuracy = method_inaccuracy(method_2_1, start, end)
else:
    method_absolute_inaccuracy, method_relative_inaccuracy = '-', '-'
print("Погрешности метода 3/8:")
print(
    f"Абсолютная погрешность при разбиении на {try_format(N1, 0)} участков: {try_format(method_absolute_inaccuracy, 0)}")
print(
    f"Относительная погрешность при разбиении на {try_format(N1, 0)} участков: {try_format(method_relative_inaccuracy, 1)}")
print()
if method_2_1 != '-':
    method_absolute_inaccuracy, method_relative_inaccuracy = method_inaccuracy(method_2_2, start, end)
else:
    method_absolute_inaccuracy, method_relative_inaccuracy = '-', '-'
print(
    f"Абсолютная погрешность при разбиении на {try_format(N2, 0)} участков: {try_format(method_absolute_inaccuracy, 0)}")
print(
    f"Относительная погрешность при разбиении на {try_format(N2, 0)} участков: {try_format(method_relative_inaccuracy, 1)}")
print()

# Сравнение погрешностей
less_accurate_method = 0  # номер менее точного метода; 0 - определить не удалось
if N1 % 3 == 0:
    _, method_1 = method_inaccuracy(method_1_1, start, end)
    _, method_2 = method_inaccuracy(method_2_1, start, end)
    if method_1 < method_2:
        less_accurate_method = 2
        print("Первый метод оказался более точным")
    elif method_2 < method_1:
        less_accurate_method = 1
        print("Второй метод оказался более точным")
    else:
        less_accurate_method = 0
        print("Погрешности равны")
elif N2 % 3 == 0:
    _, method_1 = method_inaccuracy(method_1_2, start, end)
    _, method_2 = method_inaccuracy(method_2_2, start, end)
    if method_1 < method_2:
        less_accurate_method = 2
        print("Первый метод оказался более точным")
    elif method_2 < method_1:
        less_accurate_method = 1
        print("Второй метод оказался более точным")
    else:
        less_accurate_method = 0
        print("Погрешности равны")
else:
    print("Из-за введенных данных, сравнить методы не удалось")
print()

# Реализация поиска количества разбиений для для менее точного метода
if less_accurate_method == 1:
    eps = number_input("точность эпсилон для первого метода", float)
    N = 1
    last_integ = medium_rectangles_method(N, start, end)
    new_integ = medium_rectangles_method(N * 2, start, end)
    N *= 2
    while abs(last_integ - new_integ) > eps:
        N *= 2
        last_integ = new_integ
        new_integ = medium_rectangles_method(N, start, end)
        if N >= 10 ** 10:
            N = -1
            break
    if N != -1:
        print(f"Достичь требуемой точности удалось при разбиении на {N} отрезков")
    else:
        print("Достичь требуемой точности не удалось")
elif less_accurate_method == 2:
    eps = number_input("точность эпсилон для второго метода", float)
    N = 3
    last_integ = three_and_eight_method(N, start, end)
    new_integ = three_and_eight_method(N * 2, start, end)
    N *= 2
    while abs(last_integ - new_integ) > eps:
        N *= 2
        last_integ = new_integ
        new_integ = three_and_eight_method(N, start, end)
        if N >= 10 ** 10:
            N = -1
            break
    if N != -1:
        print(f"Достичь требуемой точности удалось при разбиении на {N} отрезков")
    else:
        print("Достичь требуемой точности не удалось")
