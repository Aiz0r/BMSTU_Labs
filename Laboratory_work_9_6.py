# Насута Кирилл ИУ7-12Б
# Программа, позволяющая задать матрицы и считающая количество элементов первой матрицы больших среднего арифметического второй

# Ввод
rows = -1
cols = -1
while cols <= 0 or rows <= 0:
    rows = int(input("Введите количество строк матрицы: \n"))
    cols = int(input("Введите количество столбцов матрицы: \n"))

print("Ввод матрицы:")
array = [[0] * cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        array[i][j] = input(f"Введите строку массива с индексом строки {i} и индексом столбца {j}: \n")

# Вывод введенной матрицы
print("Введенная матрица:")
for i in range(rows):
    for j in range(cols):
        print(f"{array[i][j]: >16}", end=' ')
    print()
print()
# Реализация
vowels = 'AEIOUY'
consonants = "qwrtpsdfghklzxcvbnm"
for i in range(rows):
    for j in range(cols):
        for str_el in vowels:
            array[i][j] = array[i][j].replace(str_el, str_el.lower())
        for str_el in consonants:
            array[i][j] = array[i][j].replace(str_el, str_el.upper())

# Вывод
print("Полученная матрица: ")
for i in range(rows):
    for j in range(cols):
        print(f"{array[i][j]: >16}", end=' ')
    print()
