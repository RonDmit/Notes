import os.path
import ReadShow
import AddNote

def find_note(file_base, choiсe):
    if not os.path.isfile(file_base):
        print('Записная книжка пуста')
        return
    base = ReadShow.read_record(file_base)
    index = answer()
    info = input(f"Введите, что ищете: ")
    current_index = 0
    check_operation = False
    while current_index < len(base):
        arr = base[current_index].split(';')
        if arr[index].strip() == info:
            check_operation = True
            if choiсe == 1:
                show_note(base[current_index])
            if choiсe == 2:
                print('Удаленa запись:')
                show_note(base[current_index])
                del base[current_index]
                current_index -= 1
                newFile(file_base, base)
            if choiсe == 3:
                del_note = base[current_index]
                del base[current_index]
                input_note = AddNote.enter_note(file_base, 0)
                base.append(input_note)
                print("Вы заменили запись:")
                print(del_note)
                print('на')
                print(input_note)
                print('-------------------------')
                newFile(file_base, base)
                break
        current_index += 1
    if check_operation == False:
        print('Нет такой записи')
        print('-------------------------')

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
    print(f'Запись с индификационным номером {arr[0]}')
    print(f'Заголовок: {arr[1]}')
    print(f'Текст записи: {arr[2]}')
    print(f'Дата создания: {arr[3]}\n-------------------------')

def newFile(file_base, base):
    file = open(file_base, 'w', encoding='utf-8')
    for j in base:
        file.write(j)
        file.write("\n")