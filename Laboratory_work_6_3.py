# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и находящая значение K-го экстремума в списке

# Ввод
array = list(map(int, input("Введите элементы cписка через пробел: ").split()))
k = float(input("Введите номер экстремума: "))

# Проверка ввода на корректность
if int(k) != k or k <= 0 or len(array) < k:
    print("Введенные данные некорректны")
else:

    # Поиск экстремума
    counter = 0
    k = int(k)
    el = None
    for i in range(1, len(array)-1):
        if (array[i] > array[i-1] and array[i] > array[i+1]) or (array[i] < array[i-1] and array[i] < array[i+1]):
            counter += 1
            if counter == k:
                el = array[i]
                break

    # Вывод
    if el != None:
        print(f"Значение {k:g}-го экстремума в списке равно {el:g}")
    else:
        print(f"Не удалось найти требуемый экстремум")