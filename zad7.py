# Входные данные: массив из точек с двумя координатами ((1, 2), (2, 3) …). Требуется
# вернуть массив, в котором к каждой точке будет прибавлена другая, ближайшая точка.

import random
import math


# Функция для вычисления расстояния между точками
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Функция, которая добавляет к каждой точке ближайшую точку
def add_nearest_points(points):
    return [(point[0] + min((p for p in points if p != point), key=lambda p: distance(point, p))[0],
             point[1] + min((p for p in points if p != point), key=lambda p: distance(point, p))[1])
            for point in points]


def input_points():
    num_points = int(input("Введите количество точек: "))
    points = []
    while True:
        for j in range(num_points):
            try:
                x = int(input(f"Введите x-координату точки {j + 1}: "))
                y = int(input(f"Введите y-координату точки {j + 1}: "))
                points.append((x, y))
            except ValueError:
                print("Ошибка: Введите целые числа.")
                return None
        return points


def generate_points(num_points):
    while True:
        try:
            a = int(input("Введите минимальное значение чисел: "))
            b = int(input("Введите максимальное значение чисел: "))
        except ValueError:
            print("Ошибка: Введите целые числа.")
            return None
        return [(random.uniform(a, b), random.uniform(a, b)) for _ in range(num_points)]


def show_points(points):
    for n, point in enumerate(points):
        print(f"Точка {n + 1}: ({point[0]}, {point[1]})")


def main_zad7():
    points = []

    while True:
        print("Меню:")
        print("1. Вывести условие")
        print("2. Ввести массив точек")
        print("3. Сгенерировать массив точек")
        print("4. Получить результат")
        print("5. Выход из программы")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("Входные данные: массив из точек с двумя координатами ((1, 2), (2, 3) …). "
                  "Требуется вернуть массив, в котором к каждой точке будет прибавлена другая, ближайшая точка.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "2":
            points = input_points()
            if points is not None:
                print("Точки введены.\n")
                show_points(points)
                input("Нажмите Enter, чтобы продолжить...")
        elif choice == "3":
            num_points = int(input("Введите количество точек: "))
            points = generate_points(num_points)
            print("Точки сгенерированы.\n")
            show_points(points)
            input("Нажмите Enter, чтобы продолжить...")
        elif choice == "4":
            if not points:
                print("Ошибка: Сначала введите или сгенерируйте массив точек.")
            else:
                result_points = add_nearest_points(points)
                print("Результат:")
                show_points(result_points)
                input("Нажмите Enter, чтобы продолжить...")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    pass
