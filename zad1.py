# Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму
# чисел из массивов, первый массив должен быть отсортирован в порядке убывания,
# второй в порядке возрастания. Если числа в массивах совпадают, их сумма будет равна
# нулю. Конечный массив нужно отсортировать в порядке возрастания.

import random


def sum_sorted_arrays(arr1, arr2):
    # Отсортируем первый массив в порядке убывания
    sorted_arr1 = sorted(arr1, reverse=True)
    # Отсортируем второй массив в порядке возрастания
    sorted_arr2 = sorted(arr2)

    # Вывод отсортированных массивов
    print("Первый массив (отсортирован по убыванию):", sorted_arr1)
    print("Второй массив (отсортирован по возрастанию):", sorted_arr2)

    # Произведем суммирование отсортированных массивов
    result = [x + y for x, y in zip(sorted_arr1, sorted_arr2)]
    # Отсортируем итоговый массив в порядке возрастания
    result.sort()

    return result


def input_array(value):
    try:
        arr = []
        for _ in range(value):
            num = int(input("Введите число: "))
            arr.append(num)
        return arr
    except ValueError:
        print("Ошибка: Введите только целые числа.")
        return None


def generate_array(size):
    while True:
        try:
            a = int(input("Введите минимальное значение чисел: "))
            b = int(input("Введите максимальное значение чисел: "))
        except ValueError:
            print("Ошибка: Введите целые числа.")
            return None
        return [random.randint(a, b) for _ in range(size)]


def main_zad1():
    while True:
        print("Меню:")
        print("1. Вывести условие")
        print("2. Ввести массивы вручную")
        print("3. Заполнить массивы автоматически")
        print("4. Получить результат")
        print("5. Выход из программы")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print(f"Входные данные: 2 массива с числами одинакового размера.\n"
                  f"Производится суммирование чисел из массивов.\n"
                  f"Первый массив сортируется в порядке убывания, второй - в порядке возрастания.\n"
                  f"Если числа в массивах совпадают, их сумма равна нулю.\n"
                  f"Итоговый массив сортируется в порядке возрастания.\n"
                  f"Нажмите Enter, чтобы продолжить...")
        elif choice == "2":
            size = int(input("Введите размер массива: "))
            print("Первый массив")
            arr1 = input_array(size)
            print("Второй массив")
            arr2 = input_array(size)
            if arr1 is not None and arr2 is not None and len(arr1) == len(arr2):
                print("Массивы введены вручную.")
                print("Первый массив (до сортировки):", arr1)
                print("Второй массив (до сортировки):", arr2)
                input("Нажмите Enter, чтобы продолжить...")
        elif choice == "3":
            size = int(input("Введите размер массивов: "))
            arr1 = generate_array(size)
            arr2 = generate_array(size)
            print("Массивы сгенерированы автоматически.")
            print("Первый массив (до сортировки):", arr1)
            print("Второй массив (до сортировки):", arr2)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "4":
            if "arr1" not in locals() or "arr2" not in locals():
                print("Ошибка: Сначала введите или сгенерируйте массивы.")
                continue
            result_arr = sum_sorted_arrays(arr1, arr2)
            print("Результат (отсортированный по возрастанию):", result_arr)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    pass
