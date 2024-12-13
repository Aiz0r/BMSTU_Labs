# Насута Кирилл ИУ7-12Б Программа, сортирующая массив методом расчески и считающая время сортировки

from Laboratory_func import *

# Ввод
length = number_input("длину заданного массива", int)
arr = mas_input(length, int)
n1 = -1
n2 = -1
n3 = -1
while n1 <= 0:
    n1 = number_input("первую длину массива для сравнения", int)
while n2 <= 0:
    n2 = number_input("вторую длину массивов для сравнения", int)
while n3 <= 0:
    n3 = number_input("третью длину массивов для сравнения", int)

# Вывод отсортированного массива
print("\n Отсортированный введенный массива:")
arr, _, _ = brush_sort(arr, length)
mas_output(arr, length)

# Вывод таблицы
print("-" * 84 * 2)
print("|" + " " * 40 + "|" + f"{n1: ^40}" + " |" + f"{n2: ^40}" + " |" + f"{n3: ^40}" + " |")
print("-" * 84 * 2)
print("|" + " " * 40 + "|" + (f"{'время': ^20}" + "|" + f"{'перестановки': ^20}" + "|") * 3)
print("-" * 84 * 2)

print("|" + f'{'Упорядоченный список': ^40}' + "|", end='')
_, perm, time = brush_sort(sorted_mas(n1), n1)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(sorted_mas(n2), n2)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(sorted_mas(n3), n3)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
print()
print("-" * 84 * 2)

print("|" + f'{'Cлучайный список': ^40}' + "|", end='')
_, perm, time = brush_sort(random_mas(n1), n1)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(random_mas(n2), n2)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(random_mas(n3), n3)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
print()
print("-" * 84 * 2)

print("|" + f'{'Упорядоченный в обратном порядке': ^40}' + "|", end='')
_, perm, time = brush_sort(reversed_mas(n1), n1)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(reversed_mas(n2), n2)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
_, perm, time = brush_sort(reversed_mas(n3), n3)
print(f"{time: ^20.5f}" + "|" + f"{perm: ^20g}" + "|" , end='')
print()
print("-" * 84 * 2)
