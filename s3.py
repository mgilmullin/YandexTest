# -*- coding: utf-8 -*-
# Author: Mansur Gilmullin


# ----------------------------------------------------------------------------------------------------------------------
# Подготовка к собеседованию в Яндекс: задача "C. Удаление дубликатов"
# ----------------------------------------------------------------------------------------------------------------------
# Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
# Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный
# объем памяти в процессе работы.
# ----------------------------------------------------------------------------------------------------------------------
# Формат ввода:
# Первая строка входного файла содержит единственное число n, n ≤ 1000000.
# На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.
# ----------------------------------------------------------------------------------------------------------------------
# Формат вывода:
# Выходной файл должен содержать следующие в порядке возрастания уникальные элементы входного массива.
# ----------------------------------------------------------------------------------------------------------------------
# Пример 1:
# Ввод	Вывод
# 5     2
# 2     4
# 4     8
# 8
# 8
# 8
# ----------------------------------------------------------------------------------------------------------------------
# Пример 2:
# Ввод	Вывод
# 5     2
# 2     8
# 2
# 2
# 8
# 8
# ----------------------------------------------------------------------------------------------------------------------


def Task3(inpFile="input.txt"):
    result = []  # массив для списка уникальных элементов
    # получаем входные параметры из файла и читаем данные построчно:
    with open(inpFile, "r", encoding="UTF-8") as fH:
        i = 0  # счётчик строк во входном файле
        n = 1  # предварительное количество элементов
        # Читаем файл построчно, сравниваем очередной элемент и содержимое списка result, если элемента там нет - добавляем его:
        while True and i <= n:
            line = fH.readline()
            if not line:
                break  # если достигли конца файла - также выходим из цикла

            try:
                number = int(line)  # очередная строка входного файла - число

            except Exception as e:
                number = line

            if i == 0:
                n = number  # в первой строке всегда число n - количество элементов массива, n <= 1000000
                i += 1
                continue

            if result:
                if str(number) + "\n" != result[-1]:
                    result.append(str(number) + "\n")  # если элемента в списке нет - добавляем его сразу как строку

            else:
                result.append(str(number) + "\n")

            i += 1

    with open("output.txt", "w", encoding="UTF-8") as fH:
        fH.writelines(result)

    return result


if __name__ == "__main__":
    res = Task3(inpFile="input.txt")
    # for item in res:
    #     print(item.rstrip("\n"))
