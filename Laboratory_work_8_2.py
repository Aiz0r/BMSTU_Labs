# Насута Кирилл ИУ7-12Б Программа, позволяющая задать задать матрицу и переставляющая местами строки с наибольшим и наименьшим количеством отрицательных элементов

# Ввод
lines = int(input("Введите количество строк матрицы: "))
col = int(input("Введите количество столбцов: "))

if lines <= 0 or col <= 0:
    print("Введення размерность матрицы некорректна")
else:
    a = [[0] * col for i in range(lines)]
    for i in range(lines):
        for j in range(col):
            a[i][j] = int(input(f"Введите элемент массива с индексом строки {i} и индексом столбца {j}: "))

    print("Введенная матрица:")
    for i in range(lines):
        for j in range(col):
            print(a[i][j], end=' ')
        print()

    # Реализация
    current_amount = 0
    min_amount = col + 1
    min_string_ind = -1
    max_amount = -1
    max_string_ind = -1

    for i in range(lines):
        for j in range(col):
            if a[i][j] < 0:
                current_amount += 1
        if current_amount < min_amount:
            min_amount = current_amount
            min_string_ind = i
        if current_amount > max_amount:
            max_amount = current_amount
            max_string_ind = i
        current_amount = 0

    # Смена местами
    for j in range(col):
        a[min_string_ind][j], a[max_string_ind][j] = a[max_string_ind][j], a[min_string_ind][j]

    # Вывод
    print("Полученная матрица:")
    for i in range(lines):
        for j in range(col):
            print(a[i][j], end=' ')
        print()
