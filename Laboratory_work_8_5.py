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
    max_el = None
    min_el = None

    for i in range(lines):
        for j in range(col):
            if i + 1 == j:
                if max_el == None or a[i][j] > max_el:
                    max_el = a[i][j]
            if i - 1 + j == col - 1:
                if min_el == None or a[i][j] < min_el:
                    min_el = a[i][j]

    # Вывод
    print(f"Максимальное значение в квадратной матрице над главной диагональю: {max_el}\nМинимальное значение в квадратной матрице под побочной диагональю: {min_el}")