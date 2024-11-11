# Функция ввода одномерного массива
def create_mas(length):
    array = [0] * length
    for i in range(length):
        array[i] = int(input(f"Введите элемент с индексом {i}: \n"))
    return array


# Функция ввода двумерного массива
def create_matrix(rows, cols):
    array = [[0] * cols for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            array[i][j] = int(input(f"Введите элемент массива с индексом строки {i} и индексом столбца {j}: \n"))
    return array


# Функция вывода двумерного массива
def mas_output(array, rows, cols):
    for i in range(rows):
        for j in range(cols):
            print(f"{array[i][j]: >8g}", end=' ')
        print()


# Функция вывода одномерного массива
def line_mas_output(array, length):
    for i in range(length):
        print(f"{array[i]: >8g}", end=' ')
    print()
