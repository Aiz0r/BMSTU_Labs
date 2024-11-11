# Насута Кирилл ИУ7-12Б Программа, позволяющая задать трехмерную матрицу и выводящая срез массива по большему измерению
import Laboratory_work_9_func

# Ввод
rows = -1
cols = -1
height = -1
while cols <= 0 or rows <= 0 or height <= 0:
    rows = int(input("Введите количество строк матрицы: \n"))
    cols = int(input("Введите количество столбцов матрицы: \n"))
    height = int(input("Введите длину массива: \n"))
print("Ввод трехмерной матрицы:")
array = [[[0 for m in range(height)] for j in range(cols)] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        for m in range(height):
            array[i][j][m] = int(input(f"Введите элемент массива с координатами с x = {i} y = {j} z = {m}: \n"))

# Реализация вывода среза
max_dimension = max([rows, cols, height])
print("Срез массива по большему измерению")
if max_dimension == rows:
    for j in range(cols):
        for m in range(height):
            print(array[rows // 2][j][m], end = ' ')
        print()
elif max_dimension == cols:
    for i in range(rows):
        for m in range(height):
            print(array[i][cols // 2][m], end = ' ')
        print()
else:
    for i in range(rows):
        for j in range(cols):
            print(array[i][j][height // 2], end = ' ')
        print()