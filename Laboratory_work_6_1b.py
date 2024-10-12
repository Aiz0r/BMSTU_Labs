# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и добавить элемент в заданное место списка алгоритмическим способом

# Ввод
array = list(map(int, input("Введите элементы cписка через пробел: ").split()))
number = float(input("Введите целочисленное число для вставки: "))
index = float(input("Введите индекс числа для вставки: "))

# Проверка ввода на корректность
if int(number) != number or int(index) != index or index < 0 or len(array) < index:
    print("Введенные данные некорректны")
else:

    # Добавление элемента
    number = int(number)
    index = int(index)
    array.append(None)
    last_num = array[index]
    array[index] = number
    for i in range(index + 1, len(array)):
        array[i], last_num = last_num, array[i]

    # Вывод
    print("Получившийся список: ", end='')
    for i in array:
        print(format(i, 'g') + " ", end='')

