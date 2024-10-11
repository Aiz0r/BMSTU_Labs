# Насута Кирилл ИУ7-12Б. Программа, вычисляющая значения заданной последовательности

# Ввод данных
input_error_flag = True
accuracy = float(input("Введите требуемую точность: "))
if accuracy > 0.25:
    print("Введенные данные некорректны. Точность превышает первое число последовательности")
    input_flag = False

if input_error_flag:
    max_iterations = float(input("Введите максимальное количество итераций: "))
    if max_iterations <= 0 or int(max_iterations) != max_iterations:
        print("Введенные данные некорректны. Максимальное количество итераций не является целым положительным числом")
        input_flag = False

if input_error_flag:
    step = float(input("Введите шаг печати: "))
    if step <= 0 or int(step) != step:
        print("Введенные данные некорректны. Шаг печати не является целым положительным числом")
        input_flag = False

if input_error_flag:
    # Основная часть
    n = 0
    elements_sum = 0
    accuracy_flag = False
    print("---------------------------------------------- \n|      №       |      t       |      s       |\n|--------------------------------------------|")
    while n < max_iterations:
        n += 1
        element = 1 / (3 * n - 1) ** 2
        if element < accuracy:
            accuracy_flag = True
            break
        elements_sum += element
        if (n - 1) % step == 0:
            print(f"|{n:^14}|{element:^14.6f}|{elements_sum:^14.6f}|")
    print("---------------------------------------------- ")

    # Вывод результата
    if accuracy_flag:
        print(
            f"Сумма бесконечного ряда равна {elements_sum: .6f}, она была достигнута за {n} итераций")
    else:
        print("Указанное число итераций необходимой точности достичь не удалось")
