import os.path
import ReadShow

def find_note(file_base, choiсe):
    if not os.path.isfile(file_base):
        print('Записная книжка пуста')
        return
    base = ReadShow.read_record(file_base)
    index = answer()
    info = input(f"Введите, что ищете: ")
    for i in range(len(base)):
        arr = base[i].split(';')
        if arr[index].strip() == info:
            if choiсe == 1:
                show_note(base[i])

def answer():
    play = True
    index = -1
    while play:
        answer = input("По какому параметру хотите найти запись: \n"
                       "1. ID\n"
                       "2. Заголовок\n"
                       "3. Текст\n"
                       "4. Дата\n"
                       "5. Выход\n")
        match answer:
            case "1":
                index = 0
                play = False
            case "2":
                index = 1
                play = False
            case "3":
                index = 2
                play = False
            case "4":
                index = 3
                play = False
            case "5":
                print("Вы не выбрали метод нахождения")
                play = False
            case _:
                print("Введен некорректный ответ\n")
    return index

def show_note(note):
    arr = note.split(';')
    print(f'\nЗапись с индификационным номером {arr[0]}')
    print(f'Заголовок: {arr[1]}')
    print(f'Текст записи: {arr[2]}')
    print(f'Дата создания: {arr[3]}\n')

