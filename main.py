def main_menu(file_base):
    play = True
    while play:
        answer = input("Запиская книжка: \n"
                       "1. Показать все записи\n"
                       "2. Добавить запись\n"
                       "3. Удалить запись\n"
                       "4. Изменить запись\n"
                       "5. Найти запись\n"
                       "6. Выход\n")
        match answer:
            case "1":
                print("Метод показа")
            case "2":
                print("Метод добавления")
            case "3":
                print("Метод удаления")
            case "4":
                print("Метод изменения")
            case "5":
                print("Метод нахождения")
            case "6":
                print("Вы вышли из записной книжки")
                play = False
            case _:
                print("Try again!\n")
file_base = "base.csv"
main_menu(file_base)