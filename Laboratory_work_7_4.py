# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и заменяющая в элементах списка все строчные гласные английские буквы на заглавные

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
    vowels = 'aeiouy'
    for i in range(n):
        for str_el in vowels:
            array[i] = array[i].replace(str_el, str_el.upper())

    # Вывод
    print("Получившийся список: ", end='')
    for i in array:
        print(i + " ", end='')
