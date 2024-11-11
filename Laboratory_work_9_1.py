# Насута Кирилл ИУ7-12Б Программа, позволяющая задать два массива и задать из нее матрицу, посчитав количество полных квадратов и записав в массив
import Laboratory_work_9_func

# Ввод
a_length = -1
while a_length <= 0:
    a_length = int(input("Введите длину массива A: \n"))
a = Laboratory_work_9_func.create_mas(a_length)

b_length = -1
while b_length <= 0:
    b_length = int(input("Введите длину массива B: \n"))
b = Laboratory_work_9_func.create_mas(b_length)

# Реализация
m = [[0] * b_length for i in range(a_length)]
s = [0] * a_length
curr_amount = 0
for i in range(a_length):
    for j in range(b_length):
        m[i][j] = a[i] * b[j]
        if float(a[i] * b[j]) == (a[i] * b[j]) ** 0.5 * (a[i] * b[j]) ** 0.5:
            curr_amount += 1
    s[i] = curr_amount
    curr_amount = 0

# Вывод
print("Полученная матрица: ")
for i in range(a_length):
    for j in range(b_length):
        print(f"{m[i][j]: >8g}", end=' ')
    print(f"{s[i]: >8g}")
