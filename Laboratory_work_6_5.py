# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и меняющая местами последний четный и минимальный положительный элемент

# Ввод
err_flag = False
n = float(input("Введите количество элементов списка: "))

if int(n) != n or n <= 0:
    print("Введенное количество элементов некорректно")
    err_flag = True

if not err_flag:
    array = [0] * n
    for i in range(int(n)):
        el = int(input(f"Введите элемент с индексом {i}: "))
        array.append(el)

# Замена местами элементов массива
if not err_flag:
    last_even_index = -1
    min_positive_index = -1
    min_positive = None

    # Идем с конца, следовательно ищем первый четный с конца
    for i in range(len(array) - 1, -1, -1):
        # поиск последнего четного
        if last_even_index == -1 and abs(array[i]) % 2 == 0:
            last_even_index = i
        # поиск минимального положительного
        if array[i] > 0 and (min_positive is None or array[i] < min_positive):
            min_positive = array[i]
            min_positive_index = i

    # Проверка на ненайденные значения, иначе замена
    if last_even_index == -1:
        print("В cписке не найдено четных элементов")
    else:
        if min_positive_index == -1:
            print("В списке не найдено положительных элементов")
        else:
            array[min_positive_index], array[last_even_index] = array[last_even_index], array[min_positive_index]

    # Вывод
    print("Получившаяся последовательность: ", end='')
    for i in array:
        print(format(i, 'g') + " ", end='')
