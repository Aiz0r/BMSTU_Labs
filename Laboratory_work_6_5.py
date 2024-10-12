# Насута Кирилл ИУ7-12Б Программа, позволяющая задать список и меняющая местами последний четный и минимальный положительный элемент

# Ввод
array = list(map(int, input("Введите элементы cписка через пробел: ").split()))

# Замена местами элементов массива

last_even_index = -1
min_positive_index = -1
min_positive = 1e9


for i in range(len(array)-1, -1, -1):
    if last_even_index == -1 and abs(array[i]) % 2 == 0:
        last_even_index = i
    if array[i] > 0 and array[i] < min_positive:
        min_positive = array[i]
        min_positive_index = i

if last_even_index == -1:
    print("В cписке не найдено четных элементов")
else:
    if min_positive_index == -1:
        print("В списке не найдено положительных элементов")
    else:
        array[min_positive_index], array[last_even_index] = array[last_even_index], array[min_positive_index]

# Вывод

print("Получившаяся последовательность: ", end='')
for i in array:
    print(format(i, 'g') + " ", end='')

