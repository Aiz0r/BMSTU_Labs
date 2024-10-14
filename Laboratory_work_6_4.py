# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и находящая наиболее длинную непрерывную последовательность знакочередующихся четных чисел

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
    subseq = []
    max_sub = []
    for i in range(len(array)):
        if abs(array[i]) % 2 == 0:
            if len(subseq) == 0:
                subseq.append(array[i])
            else:
                if subseq[-1] * array[i] < 0:
                    subseq.append(array[i])
                else:
                    if len(max_sub) < len(subseq):
                        max_sub = subseq
                    subseq = []
        else:
            if len(max_sub) < len(subseq):
                max_sub = subseq
            subseq = []
    if len(max_sub) < len(subseq):
        max_sub = subseq

    # Вывод

    print("Наибольная непрерывная последовательность знакочередующихся четных чисел заданной последовательности: ", end='')
    for i in max_sub:
        print(format(i, 'g') + " ", end='')

