# Насута Кирилл ИУ7-12Б Программа, позволяющая задать матрицу и транспонирующая ее
# Ввод
lines = int(input("Введите размерность квадратной матрицы: "))
col = lines

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
    for i in range(lines):
        for j in range(i, col):
            a[i][j], a[j][i] = a[j][i], a[i][j]

    # Вывод
    print("Полученная матрица:")
    for i in range(lines):
        for j in range(col):
            print(f"{a[i][j]: ^5g}", end=' ')
        print()
