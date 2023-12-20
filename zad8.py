# Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих
# чисел. Также, число будет считаться общим, если оно входит в один массив, а в другом
# массиве находится его перевернутая версия.

import random
from functools import reduce


def count_common_numbers(arr1, arr2):
    set1 = set(arr1)  # Преобразуем первый массив в множество
    set2 = set(arr2)  # Преобразуем второй массив в множество

    # Функция, которая проверяет, является ли число общим
    def is_common_number(num):
        return num in set2 or int(str(num)[::-1]) in set2

    # Фильтруем первый массив и оставляем только общие числа
    common_numbers = filter(is_common_number, set1)

    # Считаем количество общих чисел с помощью функции reduce
    common_count = reduce(lambda x, _: x + 1, common_numbers, 0)

    return common_count


def manual_input():
    while True:
        try:
            size = int(input("Введите размер массивов: "))
            arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
            arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

            # Проверяем, что размерности массивов совпадают
            if len(arr1) != size or len(arr2) != size:
                print("Ошибка: Размерности массивов не совпадают.")
                return [], []

            print("Массивы введены вручную.")
            return arr1, arr2
        except ValueError:
            print("Ошибка: Введите целое число для размерности и только целые числа и пробелы для элементов.")


def auto_input():
    while True:
        try:
            size = int(input("Введите размер массивов: "))
            min_num = int(input("Введите минимальное значение чисел: "))
            max_num = int(input("Введите максимальное значение чисел: "))
        except ValueError:
            print("Ошибка: Введите целые числа.")
            return None

        arr1 = [random.randint(min_num, max_num) for _ in range(size)]
        arr2 = [random.randint(min_num, max_num) for _ in range(size)]

        print("Массив 1:")
        print(*arr1)
        print("Массив 2:")
        print(*arr2)

        return arr1, arr2


def print_arrays(arr1, arr2):
    print("Массив 1:", arr1)
    print("Массив 2:", arr2)


def main_zad8():
    arr1 = []
    arr2 = []

    while True:
        print("\nГлавное меню:")
        print("1. Вывести условие")
        print("2. Ввести массивы вручную")
        print("3. Заполнить массивы автоматически")
        print("4. Посчитать количество общих чисел")
        print("5. Выход из программы")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("Входные данные: 2 массива с числами.")
            print("Требуется проверить, сколько у массивов общих чисел.")
            print("Число также считается общим, если оно входит в один массив"
                  " и его перевернутая версия есть во втором массиве.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "2":
            arr1, arr2 = manual_input()
            input("Нажмите Enter, чтобы продолжить...")
            print_arrays(arr1, arr2)
        elif choice == "3":
            arr1, arr2 = auto_input()
            print("Массивы заполнены автоматически.")
            input("Нажмите Enter, чтобы продолжить...")
            print_arrays(arr1, arr2)
        elif choice == "4":
            common_count = count_common_numbers(arr1, arr2)
            print(f"Количество общих чисел: {common_count}")
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    pass
