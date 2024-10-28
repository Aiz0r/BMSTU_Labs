# Насута Кирилл ИУ7-12Б Программа, позволяющая задать задать матрицу и находящая столбец с наибольшим количеством нулевых аргументов
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
    max_amount = -1
    max_col_ind = -1
    for j in range(col):
        for i in range(lines):
            if a[i][j] == 0:
                current_amount += 1
        if current_amount > max_amount:
            max_col_ind = j
            max_amount = current_amount
        current_amount = 0

    # Вывод
    print(f"Первый столбец, содержащий наибольшее количество нулевых элементов, имеет индекс {max_col_ind}")
