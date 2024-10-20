# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и находящая наиболее длинную непрерывную последовательность знакочередующихся четных чисел
from array import array

# Ввод
err_flag = False
n = float(input("Введите количество элементов списка: "))

if int(n) != n or n <= 0:
    print("Введенное количество элементов некорректно")
    err_flag = True

if not err_flag:
    array = []
    for i in range(int(n)):
        el = int(input(f"Введите элемент с индексом {i}: "))
        array.append(el)

if not err_flag:
    # Поиск подпоследовательности
    last_subseq = None

    # Индексы начала и конца подстроки для вывода
    first_ind = -1
    last_ind = -1
    first_max_ind = -1
    last_max_ind = -1

    current_len = 0
    max_sub_len = 0
    for i in range(len(array)):
        if abs(array[i]) % 2 == 0:
            if current_len == 0:
                last_subseq = array[i]
                first_ind = i
                current_len += 1
            else:
                if last_subseq * array[i] < 0:
                    last_subseq = array[i]
                    current_len += 1
                else:
                    last_ind = i
                    if max_sub_len < current_len:
                        first_max_ind = first_ind
                        last_max_ind = last_ind
                        max_sub_len = current_len
                    last_subseq = array[i]
                    first_ind = i
        else:
            last_ind = i
            if max_sub_len < current_len:
                first_max_ind = first_ind
                last_max_ind = last_ind
                max_sub_len = current_len
            last_subseq = array[i]
            first_ind = i

    # Проверка последней строки
    last_ind = len(array)
    if max_sub_len < current_len:
        first_max_ind = first_ind
        last_max_ind = last_ind
        max_sub_len = current_len

    # Вывод
    if first_max_ind != -1:
        print("Наибольная непрерывная последовательность знакочередующихся четных чисел заданной последовательности: ", end='')
        for i in range(first_max_ind, last_max_ind):
            print(format(array[i], 'g') + " ", end='')
    else:
        print("Такой последовательности не нашлось")
