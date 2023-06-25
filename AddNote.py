import datetime
import os.path
import ReadShow
def enter_note(file_base, check_id):
    parametrs = ['Заголовок', 'Информация']
    contact = add_id(file_base, check_id) + "; "
    for i in parametrs:
        while True:
            info = check_input(f"Введите {i} ")
            if info.strip():
                contact += info + "; "
                break
    current_data = datetime.datetime.now().strftime("%x")
    contact += current_data
    contact.strip()
    return contact
def write_note(file_base, check_id):
    contact = enter_note(file_base, check_id)
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(contact + '\n')
    return

def add_id(file_base, check_id):
    id = check_input('Введите ID: ')
    if check_id == False:
        return id
    if not os.path.isfile(file_base):
        return id
    base = ReadShow.read_record(file_base)
    while 1:
        for i in range(len(base)):
            arr = base[i].split(';')
            if id == arr[0]:
                id = check_input("Такой ID есть, введите другой ID: ")
                break
        break
    return id
def check_input(message):
    flag = True
    note = ""
    while flag:
        note = input(message).strip()
        if note == "":
            print("Вы ничего не ввели")
            continue
        if note.find(';') != -1:
            print("Вы ввели некорректный символ - ;")
            continue
        flag = False
    return note

