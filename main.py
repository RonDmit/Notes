import ReadShow
import AddNote
import FindChangeRemove
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
                ReadShow.show_all(file_base)
            case "2":
                AddNote.write_note(file_base, 1)
            case "3":
                FindChangeRemove.find_note(file_base, 2)
            case "4":
                FindChangeRemove.find_note(file_base, 3)
            case "5":
                FindChangeRemove.find_note(file_base, 1)
            case "6":
                print("Вы вышли из записной книжки")
                play = False
            case _:
                print("Попробуй снова!\n")
file_base = "base.csv"
main_menu(file_base)