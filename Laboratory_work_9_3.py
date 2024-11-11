# Насута Кирилл ИУ7-12Б Программа, позволяющая задать матрицы и считающая количество элементов первой матрицы больших среднего арифметического второй
import Laboratory_work_9_func

# Ввод
a_rows = -1
b_rows = -1
cols = -1
while a_rows <= 0 or b_rows <= 0 or cols <= 0:
    a_rows = int(input("Введите количество строк матрицы А: \n"))
    b_rows = int(input("Введите количество строк матрицы B: \n"))
    cols = int(input("Введите количество столбцов: \n"))
print("Ввод матрицы А: ")
a = Laboratory_work_9_func.create_matrix(a_rows, cols)
print("Ввод матрицы B: ")
b = Laboratory_work_9_func.create_matrix(b_rows, cols)

# Реализация
mas_of_amount = [0] * cols
for j in range(cols):
    sum_of_b_cols = 0
    for i in range(b_rows):
        sum_of_b_cols += b[i][j]
    arithmetic_mean_b = sum_of_b_cols / b_rows
    for i in range(a_rows):
        if float(a[i][j]) > arithmetic_mean_b:
            mas_of_amount[j] += 1

# Вывод промежуточных значений
print("Матрица А:")
Laboratory_work_9_func.mas_output(a, a_rows, cols)
print("Матрица B:")
Laboratory_work_9_func.mas_output(b, b_rows, cols)
for i in range(cols):
    print(f"Для столбца c индексом {i} количество элементов больших ср. арифметического равно: {mas_of_amount[i]}")

# Реализация второй части программы
for j in range(cols):
    for i in range(b_rows):
        if mas_of_amount[j] != 0:
            b[i][j] *= mas_of_amount[j]

# Вывод конечной матрицы B
print("Матрица B:")
Laboratory_work_9_func.mas_output(b, b_rows, cols)
