# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и находящая значение K-го экстремума в списке

# Ввод
err_flag = False
n = float(input("Введите количество элементов списка: "))

if int(n) != n or n <= 3:
    print("Введенное количество элементов некорректно")
    err_flag = True

if not err_flag:
    array = []
    for i in range(int(n)):
        el = int(input(f"Введите элемент с индексом {i}: "))
        array.append(el)

k = float(input("Введите номер экстремума: "))

if int(k) != k or k <= 0:
    print("Введенное количество экстремумов некорректно")

if not err_flag:
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