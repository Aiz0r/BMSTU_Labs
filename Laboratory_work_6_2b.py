# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и удалить элемент из данного места списка

# Ввод
array = list(map(int, input("Введите элементы cписка через пробел: ").split()))
index = float(input("Введите индекс элемента списка для удаления: "))

# Проверка ввода на корректность
if int(index) != index or index < 0 or len(array) < index:
    print("Введенные данные некорректны")
else:

    # Удаление элемента
    index = int(index)
    for i in range(index, len(array) - 1):
        array[i] = array[i + 1]
    array.pop()

    print("Получившийся список: ", end='')
    for i in array:
        print(format(i, 'g') + " ", end='')
