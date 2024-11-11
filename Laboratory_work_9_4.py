# Насута Кирилл ИУ7-12Б Программа, позволяющая задать матрицы и считающая количество элементов первой матрицы больших среднего арифметического второй
import Laboratory_work_9_func

# Ввод
rows = -1
cols = -1
length = -1
while cols <= 0 or rows <= 0 or length <= 0:
    rows = int(input("Введите количество строк матрицы: \n"))
    cols = int(input("Введите количество столбцов матрицы: \n"))
    length = int(input("Введите длину массива: \n"))
print("Ввод матрицы D:")
array = Laboratory_work_9_func.create_matrix(rows, cols)
mas = [0] * length
print("Ввод массива I:")
i = 0
while length > i:
    el = int(input(f"Введите элемент массива с индексом {i}: \n"))
    if el >= 1 and el <= rows:
        mas[i] = el - 1
        i += 1

# Реализация
max_mas = [0] * length
sum_of_max = 0
for el in range(length):
    curr_row = mas[el]
    curr_max = array[curr_row][0]
    for j in range(cols):
        curr_max = max(curr_max, array[curr_row][j])
    max_mas[el] = curr_max
    sum_of_max += curr_max
arithmetic_mean = sum_of_max / length

# Вывод
print("Матрица D: ")
Laboratory_work_9_func.mas_output(array, rows, cols)
print()
print("Массив I: ")
Laboratory_work_9_func.line_mas_output(mas, length)
print()
print("Массив R: ")
Laboratory_work_9_func.line_mas_output(max_mas, length)
print()
print(f"Вычисленное среднее арифметическое максимальных элементов: {arithmetic_mean: 5g}")
