# Насута Кирилл ИУ7-12Б Программа, позволяющая задать матрицу и поворачивающая ее по часовой и против часовой стрелки
import Laboratory_work_9_func

# Ввод
size = int(input("Введите размерность квадратной матрицы: \n"))

if size <= 0:
    print("Введення размерность матрицы некорректна")
else:
    a = Laboratory_work_9_func.create_matrix(size, size)
    print("Введенная матрица:")
    Laboratory_work_9_func.mas_output(a, size, size)
    print()
    # Реализация поворота по часовой стрелке
    for i in range(size // 2):
        for j in range(size // 2 + size % 2):
            temp = a[i][j]
            a[i][j] = a[size - j - 1][i]
            a[size - j - 1][i] = a[size - i - 1][size - j - 1]
            a[size - i - 1][size - j - 1] = a[j][size - i - 1]
            a[j][size - i - 1] = temp

    # Вывод промежуточной матрицы
    print("Матрица после повотора по часовой стрелке:")
    Laboratory_work_9_func.mas_output(a, size, size)
    print()

    # Реализация повторота против часовой стрелки
    for i in range(size // 2):
        for j in range(size // 2 + size % 2):
            temp = a[i][j]
            a[i][j] = a[j][size - i - 1]
            a[j][size - i - 1] = a[size - i - 1][size - j - 1]
            a[size - i - 1][size - j - 1] = a[size - j - 1][i]
            a[size - j - 1][i] = temp

    # Вывод конечной матрицы
    print("Матрица после повотора против часовой стрелки:")
    Laboratory_work_9_func.mas_output(a, size, size)
