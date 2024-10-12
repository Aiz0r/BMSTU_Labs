# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и добавить элемент в заданное место списка

# Ввод
array = list(map(int, input("Введите элементы cписка через пробел: ").split()))
number = float(input("Введите целочисленное число для вставки: "))
index = float(input("Введите индекс числа для вставки: "))

# Проверка ввода на корректность
if int(number) != number or int(index) != index or index < 0:
    print("Введенные данные некорректны")
else:

    # Добавление элемента
    number = int(number)
    index = int(index)
    array.insert(index, number)

    # Вывод
    print("Получившийся список: ", end = '')
    for i in array:
        print(format(i, 'g') + " ", end='')
