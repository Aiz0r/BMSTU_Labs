# Насута Кирилл ИУ7-12Б Программа, позволяющая задать задать матрицу и переставляющая столбцы с максимальной и минимальной суммой

# Ввод
lines = int(input("Введите количество строк квадратной матрицы: "))
col = int(input("Введите количество квадратной столбцов: "))

if lines <= 0 or col <= 0 or col != lines:
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
    for i in range(lines):
        for j in range(i, col):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    # Вывод
    print("Полученная матрица:")
    for i in range(lines):
        for j in range(col):
            print(a[i][j], end=' ')
        print()