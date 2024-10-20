# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и удалить элемент из данного места списка

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
    index = float(input("Введите индекс числа для удаления: "))

    if int(index) != index or index < 0 or index >= len(array):
        print("Введенный индекс некорректен")
        err_flag = True

if not err_flag:

    # Удаление элемента
    index = int(index)
    for i in range(index, len(array) - 1):
        array[i] = array[i + 1]
    array.pop()
    n -= 1

    # Вывод
    print("Получившийся список: ", end='')
    for i in array:
        print(format(i, 'g') + " ", end='')
