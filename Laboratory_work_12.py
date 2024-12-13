# Насута Кирилл ИУ7-12Б Программа, позволяющая редактировать заданный текст различными способами через меню

# Функция задающая данный текст
def test_list():
    # return ['ABOBA ABOBA.   23', "*", "2", "dssadsa . das"]
    return [
        "FOO!",
        "bar foo, foo BAR.",
        "512*10",
        "-500/5",
        "Foo bar, look, Kirill!. FOO BAR MAR"
    ]

# Функция вывода массива
def text_output(arr: list):
    for i in arr:
        print(i)


# Функция информирования меню
def menu_output():
    print("Меню измениния текста:")
    print("1. Выровнять текст по левому краю")
    print("2. Выровнять текст по правому краю")
    print("3. Выровнять текст по ширине")
    print("4. Удалить все вхождения введенного слова")
    print("5. Заменить введенное слово другим введенным словом")
    print("6. Вычислить результат умножения и деления всех чисел внутри текста")
    print("7. Поиск и удаление предложения с самым коротким словом")
    print("8. Выйти из программы")
    print("***Для исполнения команды введите ее номер***")
    print()


# Функция очищающая массив от лишних пробелов
def clear_space(arr: list):
    for j in range(len(arr)):
        while arr[j].find("  ") != -1:
            arr[j] = arr[j].replace("  ", " ")
        if arr[j][0] == ' ':
            arr[j] = arr[j][1:]
        if arr[j][-1] == " ":
            arr[j] = arr[j][:-1]
    return arr


# Функция счета пробелов в строке
def amount_of_space(line: str):
    amount = 0
    for i in range(len(line)):
        if line[i] == " ":
            amount += 1
    return amount


# Функция для поиска строки максимальной длины
def max_string_len(arr: list):
    max_len = 0
    for el in arr:
        max_len = max(len(el), max_len)
    return max_len


# 3 Функции вызываемые консолью
def left_edge(arr: list):
    arr = clear_space(arr)
    for i in range(len(arr)):
        while arr[i][0] == " ":
            arr[i] = arr[i][1:]
    return arr


def right_edge(arr: list):
    arr = clear_space(arr)
    max_len = max_string_len(arr)
    for i in range(len(arr)):
        el = arr[i]
        arr[i] = abs(len(el) - max_len) * " " + el
        while arr[i][-1] == " ":
            arr[i] = arr[i][:-1]
    return arr


def middle_edge(arr: list):
    arr = clear_space(arr)
    max_len = max_string_len(arr)
    for i in range(len(arr)):
        el = arr[i]
        spaces = amount_of_space(el)
        if spaces != 0:
            if max_len != len(el):
                extra_spaces = (max_len - len(el)) // spaces
                left_spaces = (max_len - len(el)) - spaces * extra_spaces
                el = el.replace(" ", " " * (extra_spaces+1))
                if left_spaces != 0:
                    for j in range(len(el)):
                        if el[j] == " ":
                            el = el[:j] + " " * (left_spaces) + el[j:]
                            break
            arr[i] = el
    return arr


def remove_word(arr: list, remove_word: str):
    for el in range(len(arr)):
        line = arr[el]
        start_ind = 0
        i = 0
        while i < len(line):
            if line[i] == " " or line[i] == "," or line[i] == '.' or line[i] == ':' or line[i] == ';' or line[i] == "!" or line[i] == "?":
                if line[start_ind:i] == remove_word:
                    line = line[:start_ind - 1] + line[i:]
                    i -= i - start_ind
                start_ind = i + 1
            i += 1
        arr[el] = line
    return arr


def replace_word(arr: list, old_word: str, new_word: str):
    for el in range(len(arr)):
        line = arr[el]
        start_ind = 0
        i = 0
        while i < len(line):
            if line[i] == " " or line[i] == "," or line[i] == '.' or line[i] == ':' or line[i] == ';' or line[i] == "!" or line[i] == "?":
                if line[start_ind:i] == old_word:
                    line = line[:start_ind] + new_word + line[i:]
                    i += len(new_word) - len(old_word)
                start_ind = i + 1
            i += 1
        arr[el] = line
    return arr


def all_text_len(arr: list):
    text_len = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            text_len += 1
    return text_len


def remove_line_with_short_word(arr: list):
    arr = clear_space(arr)
    curr_prop = ""
    prop_start_line_ind = 0
    prop_start_point_ind = 0
    prop_short = ""
    prop_short_start_line_ind = -1
    prop_short_end_line_ind = -1
    prop_short_start_point_ind = -1
    prop_short_end_point_ind = -1
    shortest_word_flag = False

    shortest_word_ind = -1
    shortest_word_line_ind = -1
    shortest_word_len = None
    shortes_word = ""
    curr_word = ""

    # Ищем самое короткое слово и его предложения
    for line_ind in range(len(arr)):
        curr_word = ""
        for i in range(len(arr[line_ind])):
            line = arr[line_ind]
            if line[i] != " " and line[i] != "," and line[i] != "." and line[i] != ";" and line[i] != "!" and line[i] != "?":
                curr_word += line[i]
            else:
                if (shortest_word_len == None or shortest_word_len > len(curr_word)) and curr_word != "":
                    shortest_word_len = len(curr_word)
                    shortes_word = curr_word
                    shortest_word_line_ind = line_ind
                    shortest_word_ind = i - len(curr_word)
                    shortest_word_flag = True
                curr_word = ""

            if line[i] != "."  and line[i] != "!" and line[i] != "?":
                curr_prop += line[i]
            else:
                if shortest_word_flag:
                    prop_short = curr_prop
                    prop_short_start_line_ind = prop_start_line_ind
                    prop_short_end_line_ind = line_ind
                    prop_short_start_point_ind = prop_start_point_ind
                    prop_short_end_point_ind = i
                    shortest_word_flag = False
                curr_prop = ""
                prop_start_line_ind = line_ind
                prop_start_point_ind = i
        if curr_word != "" and (shortest_word_len == None or shortest_word_len > len(curr_word)):
            shortest_word_len = len(curr_word)
            shortest_word_ind = i - len(curr_word)
            shortes_word = curr_word
            shortest_word_flag = True

    if curr_word != "" and (shortest_word_len == None or shortest_word_len > len(curr_word)):
        shortest_word_len = len(curr_word)
        shortest_word_ind = i - len(curr_word)
        shortes_word = curr_word
        shortest_word_flag = True

    if shortest_word_flag and curr_prop != "":
        prop_short = curr_prop
        prop_short_start_line_ind = prop_start_line_ind
        prop_short_end_line_ind = line_ind
        prop_short_start_point_ind = prop_start_point_ind
        prop_short_end_point_ind = len(line) - 1

    # Удаляем
    if prop_short_start_line_ind == prop_short_end_line_ind:
        line = arr[prop_short_start_line_ind]
        line = line[:prop_short_start_point_ind] + line[prop_short_end_point_ind + 1:]
        arr[prop_short_start_line_ind] = line
    else:
        for line_ind in range(prop_short_start_line_ind, prop_short_end_line_ind + 1):
            line = arr[line_ind]
            if line_ind == prop_short_start_line_ind:
                line = line[:prop_short_start_point_ind]
                arr[line_ind] = line
            elif line_ind == prop_short_end_line_ind:
                line = line[prop_short_end_point_ind+2:]
                arr[line_ind] = line
            else:
                arr[line_ind] = ""
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == "" or arr[i] == ".":
            del arr[i]
    print("Самое короткое слово:", shortes_word)
    return arr


def arithmetic_operations(arr: list):
    for i in range(len(arr)):
        el = arr[i]
        j = 0
        while j < len(el):
            if el[j] == "*" or el[j] == "/":
                operation = el[j]
                right_ind = j + 1
                new_string_right_ind = 0
                new_right_string_flag = False
                right_num = ""
                if right_ind != len(el) and el[right_ind] == "-":
                    right_num += el[right_ind]
                    right_ind += 1
                while right_ind < len(el) and (el[right_ind].isdigit()):
                    right_num += el[right_ind]
                    right_ind += 1
                if right_ind == len(el):
                    if i + 1 != len(arr):
                        next_el = arr[i + 1]
                        while new_string_right_ind < len(next_el) and (next_el[new_string_right_ind].isdigit()):
                            new_right_string_flag = True
                            right_num += next_el[new_string_right_ind]
                            new_string_right_ind += 1

                left_ind = j - 1
                left_num = ""
                new_string_left_ind = -1
                new_left_string_flag = False
                minus_stop_flag = False
                while left_ind > -1 and el[left_ind].isdigit():
                    left_num += el[left_ind]
                    left_ind -= 1
                if left_ind != -1 and el[left_ind] == "-":
                    left_num += el[left_ind]
                    left_ind -= 1
                    minus_stop_flag = True

                if left_ind == -1 and not minus_stop_flag:
                    if i != 0:
                        next_el = arr[i-1]
                        new_string_left_ind = len(arr[i-1]) - 1
                        while new_string_left_ind > -1 and (next_el[new_string_left_ind].isdigit()):
                            left_num += next_el[new_string_left_ind]
                            new_string_left_ind -= 1
                            new_left_string_flag = True

                        if new_string_left_ind != -1 and next_el[new_string_left_ind] == "-":
                            left_num += next_el[new_string_left_ind]
                            new_string_left_ind -= 1
                left_num = left_num[::-1]
                if right_num != "" and left_num != "":
                    if operation == "*":
                        res = int(left_num) * int(right_num)
                    else:
                        if int(right_num) != 0:
                            res = int(left_num) // int(right_num)
                            j = left_ind - 1
                        else:
                            res = left_num + operation + right_num
                    if not new_left_string_flag and not new_right_string_flag:
                        el = el[:left_ind + 1] + str(res) + el[right_ind:]
                    else:
                        if new_right_string_flag and not new_left_string_flag:
                            el = el[:left_ind + 1] + str(res)
                            right_el = arr[i+1]
                            right_el = right_el[new_string_right_ind:]
                            arr[i+1] = right_el

                        else:
                            if not new_right_string_flag and new_left_string_flag:
                                el = str(res) + el[right_ind:]
                                left_el = arr[i-1]
                                left_el = left_el[:new_string_left_ind+1]
                                arr[i-1] = left_el
                            else:
                                el = str(res)
                                right_el = arr[i + 1]
                                right_el = right_el[new_string_right_ind:]
                                arr[i + 1] = right_el
                                left_el = arr[i - 1]
                                left_el = left_el[:new_string_left_ind + 1]
                                arr[i - 1] = left_el

            j += 1
        arr[i] = el
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == "" or arr[i] == "." or arr[i] == "?" or arr[i] == "!":
            del arr[i]
    return arr


# Реализация ввода
n = ""
arr = test_list()
menu_output()
amount_of_comands = 0
while n != '8':
    n = input("Введите номер команды: ")
    amount_of_comands += 1
    if amount_of_comands % 3 == 0:
        menu_output()
    match n:
        case "1":
            arr = left_edge(arr)
            print("Полученный текст: \n")
            text_output(arr)
        case "2":
            arr = right_edge(arr)
            print("Полученный текст: \n")
            text_output(arr)
        case "3":
            arr = middle_edge(arr)
            print("Полученный текст: \n")
            text_output(arr)
        case "4":
            word = input("Введите слово для удаления: ")
            arr = remove_word(arr, word)
            print("Полученный текст: \n")
            text_output(arr)
        case "5":
            word1 = input("Введите заменяемое слово: ")
            word2 = input("Введите слово для замены: ")
            arr = replace_word(arr, word1, word2)
            print("Полученный текст: \n")
            text_output(arr)
        case "6":
            arr = arithmetic_operations(arr)
            print("Полученный текст: \n")
            text_output(arr)
        case "7":
            arr = remove_line_with_short_word(arr)
            print("Полученный текст: \n")
            text_output(arr)
        case "8":
            break
        case _:
            print("Введенные символы не являются командой")
    print()
