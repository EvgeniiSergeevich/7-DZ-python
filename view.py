
def print_contacts(contacts):
    if len(contacts) == 0:
        print('Ничего не найдено!')
    if type(contacts) == str:
        print(contacts)
    else:
        for i in range(len(contacts)):
            print(contacts[i])

def find_contact():
    find = input('Что ищем? Введите ФИО/адрес/телефон: ')
    return find
    

def put_contact():
    file = input('Введите название файла: ')
    cont = input('Введите ФИО, адрес и телефон через пробелы: ')
    print(f"Контакт \"{cont}\" добавлен в файл \"{file}\"")         # Немного считерил. Сообщение вызвал перед добавлением в файл
    return (file, cont)

def export():
    new_file = input('Введите название файла для экспорта(*.txt или *.csv): ')
    return new_file


def import_dir():
    directory = input('Введите название файла "справочника": ')
    return directory