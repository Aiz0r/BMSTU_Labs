# Насута Кирилл ИУ7-12Б Программа, которая выводит таблицу значений функций и чертит график

from math import sin
# Входные данные
scale = 100
max_y = -1e9
min_y = 1e9

start = float(input("Введите координату начала: "))
end = float(input("Введите координату конца "))
step = float(input("Введите шаг: "))

if start > end:
    print("Введенные данные некорректны. Начальное число больше конечного")
elif step <= 0:
    print("Введенные данные некорректны. Шаг меньше 0")
else:
    print(
        "---------------------------------------------- \n|      x       |      y1      |      y2      |\n|--------------------------------------------|")
    # Приведение float к int для использования в фор for
    start = int(start * 1e9)
    step = int(step * 1e9)
    end = int(end * 1e9)
    number_of_positive_s = 0
    number_of_negative_s = 0
    for i in range(start, end + 1, step):
        b = i / 1e9
        s1 = 1.021 * b ** 3 - 3.995 * b ** 2 + 2.5
        s2 = 3.04 * b ** 3 - 2.89 * sin(5 * b) - 1.72
        if s1 < 0:
            number_of_negative_s += 1
        elif s1 > 0:
            number_of_positive_s += 1
        max_y = max(max_y, s1)
        min_y = min(min_y, s1)
        print(f"|{b:^14.6f}|{s1:^14.6f}|{s2:^14.6f}|")
    print("----------------------------------------------")

    # Решение дополнительной задачи
    print(
        f"Количество положительных значений первой функции: {number_of_positive_s}\nКоличество положительных значений первой функции: {number_of_negative_s}\n")


    marks = float(input("Введите целое количество засечек от 4 до 8: "))
    if not (4 <= marks <= 8):
        print("Введенные данные некорректны. Число засечек должно быть от 4 до 8")
    elif int(marks) != marks:
        print("Введенные данные некорректны. Число засечек должно быть целым")
    else:

        # Проверка на наличие нуля
        zero_flag = False
        if min_y * max_y < 0:
            zero_flag = True
        else:
            zero_flag = False

        # Вывод засечек
        temp_marks = 0
        marks = int(marks)
        axis_y = ""
        last_el = 0
        print(" " * 8, end='')
        while temp_marks < marks:
            #number = (max_y - min_y) / (marks - 1) * temp_marks + min_y
            #print(f"{number:.4f}" + " " * (scale // (marks-1)), end='')
            if temp_marks == 0 :
                axis_y += format(min_y, 'g')
                last_el = len(format(min_y, 'g'))
            elif temp_marks == marks - 1:
                axis_y += " " * (scale - len(axis_y)) + format(max_y, 'g')
            else:
                indent = format((max_y - min_y) // marks * temp_marks + min_y, 'g')
                axis_y += " " * (scale // (marks - 1) - last_el) + indent
                last_el = len(indent)
            temp_marks += 1
        print(axis_y)

        # Вывод графика
        for i in range(start, end + 1, step):
            b = i / 1e9
            s = 1.021 * b ** 3 - 3.995 * b ** 2 + 2.5
            indent = int(abs(s - min_y) * scale / abs(max_y - min_y))
            if zero_flag:
                zero_position = int(abs(-min_y) * scale / abs(max_y - min_y))
                print(f"{b: <7.5g}|", end='')
                if zero_position == indent:
                    print(" " * indent + "*")
                elif zero_position < indent:
                    print(" " * zero_position + "|" + " " * (indent - zero_position - 1) + "*")
                else:
                    print(" " * indent + "*" + " " * (zero_position - indent - 1) + "|")
            else:
                print(f"{b: <7.5g}|", end='')
                print(" " * indent + "*")

