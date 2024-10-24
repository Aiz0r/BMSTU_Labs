# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и ищущая строку наибольшей длины, не содержащей цифр

# Ввод
n = int(input("Введите количество элементов списка: "))

if n <= 0:
    print("Введенное количество элементов некорректно")
else:
    array = []
    for i in range(n):
        el = input(f"Введите элемент с индексом {i}: ")
        array.append(el)

    max_len_str = ""
    for i in range(n):
        el = array[i]
        length = len(el)
        checker = True
        for j in range(length):
            if '0' <= el[j] <= '9':
                checker = False
        if checker and len(max_len_str) < length:
            max_len_str = el

    # Вывод
    if max_len_str == "":
        print("В списке нет строк не содержащих цифры")
    else:
        print(f"Строка наибольшей длины, не содержащая цифр: {max_len_str}")
