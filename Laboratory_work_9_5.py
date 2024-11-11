# Насута Кирилл ИУ7-12Б Программа, позволяющая задать матрицы и находящая их произведение
import Laboratory_work_9_func


# Функция ввода размерностей для упрощения кода
def get_matrix_dimensions(matrix_name):
    rows = -1
    cols = -1
    while rows <= 0:
        rows = int(input(f"Введите количество строк матрицы {matrix_name}: \n"))
    while cols <= 0:
        cols = int(input(f"Введите количество столбцов матрицы {matrix_name}: \n"))
    return rows, cols


# Ввод
a_rows, a_cols = get_matrix_dimensions("A")
b_rows, b_cols = get_matrix_dimensions("B")

if a_cols == b_rows:
    print("Ввод матрицы А: ")
    a = Laboratory_work_9_func.create_matrix(a_rows, a_cols)
    print("Ввод матрицы B: ")
    b = Laboratory_work_9_func.create_matrix(b_rows, b_cols)

    # Реализация
    c = [[0] * b_cols for i in range(a_rows)]
    for i in range(a_rows):
        for j in range(b_cols):
            for el in range(a_cols):
                c[i][j] = a[i][el] * b[el][j]

    # Вывод
    print("Матрица А:")
    Laboratory_work_9_func.mas_output(a, a_rows, a_cols)
    print()
    print("Матрица B:")
    Laboratory_work_9_func.mas_output(b, b_rows, b_cols)
    print()
    print("Матрица C:")
    Laboratory_work_9_func.mas_output(c, a_rows, b_cols)
else:
    print("Матрицы нельзя перемножить, количество столбцов A не равно количеству строк B")
