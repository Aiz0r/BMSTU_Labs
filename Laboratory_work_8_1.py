# Насута Кирилл ИУ7-12Б Программа, позволяющая задать задать матрицу и находящая строку с наименьшим количеством четных элементов

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
            print(a[i][j], end = ' ')
        print()

    # Реализация
    current_amount = 0
    min_amount = col + 1
    min_string_ind = -1

    for i in range(lines):
        for j in range(col):
            if abs(a[i][j]) % 2 == 0:
                current_amount += 1
        if current_amount < min_amount:
            min_amount = current_amount
            min_string_ind = i
        current_amount = 0

    # Вывод
    print(f"Строка, содержащая наименьшее количество четных элементов, имеет индекс {min_string_ind}")
