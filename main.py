import zad1
import zad7
import zad8


def menu():
    while True:
        print("Главное меню:")
        print("1. Задание 1")
        print("2. Задание 7")
        print("3. Задание 8")
        print("4. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            zad1.main_zad1()
        elif choose == "2":
            zad7.main_zad7()
        elif choose == "3":
            zad8.main_zad8()
        elif choose == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    menu()
