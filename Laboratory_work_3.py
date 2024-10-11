# Насута Кирилл ИУ7-12Б Программа, определяющая по координатам вершин характеристики треугольника

# Ввод дааных
def initial_data():
    x1 = int(input("Введите координату х точки 1:"))
    y1 = int(input("Введите координату y точки 1:"))

    x2 = int(input("Введите координату х точки 2:"))
    y2 = int(input("Введите координату y точки 2:"))

    x3 = int(input("Введите координату х точки 3:"))
    y3 = int(input("Введите координату y точки 3:"))

    # проверка на то, что вершины лежат на одной прямой и не совпадают
    flag = True
    eps = 1e-8
    if abs(find_S(x1, y1, x2, y2, x3, y3)) <= eps:
        print("Введенные вами вершины не образуют треугольник")
        flag = False

    return x1, y1, x2, y2, x3, y3, flag


def initial_point_data():
    x = int(input("Введите координату х произвольной точки:"))
    y = int(input("Введите координату y произвольной точки:"))
    return x, y


# Базовые функции поиска стороны и площади по координатам
def find_side(x1, y1, x2, y2):
    side = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return side


def find_S(x1, y1, x2, y2, x3, y3):
    side12 = find_side(x1, y1, x2, y2)
    side23 = find_side(x3, y3, x2, y2)
    side31 = find_side(x1, y1, x3, y3)

    p = (side12 + side23 + side31) / 2
    S = (p * (p - side12) * (p - side23) * (p - side31)) ** 0.5

    return S


# Функция поиска длины сторон и медианвы
def sides_length(x1, y1, x2, y2, x3, y3):
    side12 = find_side(x1, y1, x2, y2)
    side23 = find_side(x3, y3, x2, y2)
    side31 = find_side(x1, y1, x3, y3)

    minside = min(side12, side23, side31)

    # Определения координат середиины стороны лежащей напротив наименьшего угла
    if minside == side12:
        medianx = (x1 + x2) / 2
        mediany = (y1 + y2) / 2

        secondx = x3
        secondy = y3
    elif minside == side23:
        medianx = (x3 + x2) / 2
        mediany = (y3 + y2) / 2

        secondx = x1
        secondy = y1
    else:
        medianx = (x3 + x1) / 2
        mediany = (y3 + y1) / 2

        secondx = x2
        secondy = y2

    median = ((medianx - secondx) ** 2 + (mediany - secondy) ** 2) ** 0.5

    return side12, side23, side31, median


def right_triangle_check(x1, y1, x2, y2, x3, y3):
    side1 = find_side(x1, y1, x2, y2)
    side2 = find_side(x3, y3, x2, y2)
    side3 = find_side(x1, y1, x3, y3)
    hypotenuse = max(side1, side2, side3)
    eps = 1e-8
    return abs(hypotenuse ** 2 - side1 ** 2 - side2 ** 2 - side3 ** 2 + hypotenuse ** 2) <= eps


def in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    eps = 1e-8
    if abs(find_S(x1, y1, x2, y2, x3, y3) - find_S(x, y, x1, y1, x2, y2) -
           find_S(x, y, x2, y2, x3, y3) - find_S(x, y, x1, y1, x3, y3)) <= eps:
        return True
    else:
        return False


def minimal_distance(x, y, x1, y1, x2, y2, x3, y3):
    h1 = 2 * find_S(x, y, x1, y1, x2, y2) / find_side(x1, y1, x2, y2)
    h2 = 2 * find_S(x, y, x2, y2, x3, y3) / find_side(x2, y2, x3, y3)
    h3 = 2 * find_S(x, y, x1, y1, x3, y3) / find_side(x1, y1, x3, y3)

    return min(h1, h2, h3)


def output():
    x1, y1, x2, y2, x3, y3, flag = initial_data()
    if flag:
        side1, side2, side3, median = sides_length(x1, y1, x2, y2, x3, y3)
        print(f"Длины сторон треугольника равны: {format(side1, 'g')}, "
              f"{format(side2, 'g')}, {format(side3, 'g')}")
        print(f"Длина медианы проведенной из наименьшего угла равна {format(median, 'g')}")
        if right_triangle_check(x1, y1, x2, y2, x3, y3):
            print("Треугольник является прямоугольным")
        else:
            print("Треугольник не является прямоугольным")

        x, y = initial_point_data()
        if in_triangle(x, y, x1, y1, x2, y2, x3, y3):
            print("\nТочка находится внутри треугольника")
            print(f"Расстояние от точки до ближайшей стороны треугольника равно: "
                  f"{format(minimal_distance(x, y, x1, y1, x2, y2, x3, y3), 'g')}")
        else:
            print("\nТочка не находится внутри треугольника")


output()

# Прямая задается двумя точками. И задается точка. От точки до прямой 