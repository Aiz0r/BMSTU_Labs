# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и добавляющая удвоенное значение после каждого целого положительного элемента

# Ввод
n = int(input("Введите количество элементов списка: "))

if n <= 0:
    print("Введенное количество элементов некорректно")
else:
    array = []
    for i in range(n):
        el = int(input(f"Введите элемент с индексом {i}: "))
        array.append(el)

    new_len = n
    amount_of_positive = 0
    for i in range(n):
        if array[i] > 0:
            amount_of_positive += 1

    array += [None] * amount_of_positive

    for i in range(n-1, -1, -1):
        if array[i] > 0:
            array[i+amount_of_positive] = array[i] * 2
            amount_of_positive -= 1
        array[i+amount_of_positive] = array[i]



    # Вывод
    print("Получившийся список: ", end='')
    for i in range(len(array)):
        print(format(array[i], 'g') + " ", end='')