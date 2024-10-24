# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и удаляющая из него все нечетные элементы

# Ввод
n = int(input("Введите количество элементов списка: "))

if n <= 0:
    print("Введенное количество элементов некорректно")
else:
    array = []
    for i in range(n):
        el = int(input(f"Введите элемент с индексом {i}: "))
        array.append(el)

    amount_of_even = 0
    i = 0
    for el in array:
        if abs(el) % 2 == 0:
            array[i] = el
            i += 1
        else:
            amount_of_even += 1
    array = array[:n-amount_of_even]

    # Вывод
    print("Получившийся список: ", end='')
    for i in range(len(array)):
        print(format(array[i], 'g') + " ", end='')