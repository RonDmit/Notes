import datetime
import os.path
import ReadShow
def enter_note(file_base):
    parametrs = ['Заголовок', 'Информация']
    contact = add_id(file_base) + "; "
    for i in parametrs:
        while True:
            info = input(f"Введите {i} ")
            if info.strip():
                contact += info + "; "
                break
    current_data = datetime.datetime.now().strftime("%x")
    contact += current_data
    contact.strip()
    with open(file_base, 'a', encoding='utf-8') as f:
        f.write(contact + '\n')
    return

def add_id(file_base):
    id = input(f"Введите ID: ").strip()
    if not os.path.isfile(file_base):
        return id
    base = ReadShow.read_record(file_base)
    while 1:
        for i in range(len(base)):
            arr = base[i].split(';')
            if id == arr[0]:
                id = input(f"Такой ID есть, введите другой ID: ").strip()
                break
        break
    return id
