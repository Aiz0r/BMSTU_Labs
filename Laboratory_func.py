# Обработка ввода
def number_input(name: str, input_type: type):
    while True:
        try:
            number = input_type(input(f"Введите {name}: "))
        except ValueError:
            if input_type == int:
                print("Введенные данные не являются целыми числом")
            else:
                print("Введенные данные не являются числом")
        else:
            break
    return number

# Получение времени выполнения ввода массива
def get_time(func):
    import time
    def action(arr, length):
        start = time.time()
        result, perm = func(arr, length)
        end = time.time()
        return result, perm, end - start
    return action

# Cортировка методом "расчески"
@get_time
def brush_sort(array, length):
    step = length
    checker = True
    perm = 0
    while step > 1 or checker:
        if step > 1:
            step -= 1
        checker = False
        i = 0
        while i + step < length:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                perm += 1
                checker = True
            i += step
    return array, perm

# Ввод массива
def mas_input(length, type):
    arr = [0]*length
    for i in range(length):
        arr[i] = number_input(f'элемент массива с индексом {i}: ', type)
    return arr

# Вывод массива
def mas_output(arr, length):
    for i in range(length):
        print(arr[i], end=' ')
    print()

# Функция создающая упорядоченный список
def sorted_mas(length):
    arr = [0] * length
    for i in range(length):
        arr[i] = i
    return arr

# Функция создания случайного списка
def random_mas(length):
    from random import randint
    arr = [0] * length
    for i in range(length):
        arr[i] = randint(0, 100)
    return arr

# Функция создания упорядоченного в обратном порядке списка
def reversed_mas(length):
    arr = [0] * length
    for i in range(length, -1, -1):
        arr[length - i - 1] = i
    return arr

