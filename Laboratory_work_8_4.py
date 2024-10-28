# Насута Кирилл ИУ7-12Б Программа, позволяющая задать задать матрицу и переставляющая столбцы с максимальной и минимальной суммой

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
            print(f"{a[i][j]: ^5g}", end=' ')
        print()

    # Реализация
    current_amount = 0
    min_sum = None
    min_col_ind = -1
    max_sum = None
    max_col_ind = -1

    for j in range(col):
        for i in range(lines):
            current_amount += a[i][j]
        if min_sum is None or current_amount < min_sum:
            min_sum = current_amount
            min_col_ind = j
        if max_sum is None or current_amount > max_sum:
            max_sum = current_amount
            max_col_ind = j
        current_amount = 0

    # Смена местами
    for i in range(lines):
        a[i][max_col_ind], a[i][min_col_ind] = a[i][min_col_ind], a[i][max_col_ind]

    # Вывод
    print("Полученная матрица:")
    for i in range(lines):
        for j in range(col):
            print(f"{a[i][j]: ^5g}", end=' ')
        print()
