import codecs
# def get_cont_full_name(first_name, second_name, last_name, contacts):
#     for i in range(len(contacts) - 1):
#         tmp = contacts[i].split()
#         if first_name == tmp[0] and second_name == tmp[1] and last_name == tmp[2]:
#             tmp1 = contacts[i]
#         else:
#             tmp1 = 'нет совпадений!'
#     return tmp1

# def get_cont_part_name(name, contacts):
#     tmp1 = []
#     for i in range(len(contacts) - 1):
#         tmp = contacts[i].split()
#         if name == tmp[0] or name == tmp[1] or name == tmp[2]:
#             tmp1.append(contacts[i])
#     return tmp1

# def get_cont_phone(phone, contacts):
#     for i in range(len(contacts) - 1):
#         tmp = contacts[i].split()
#         if phone == int(tmp[-1]):
#             tmp1 = contacts[i]
#     return tmp1

# def get_cont_addres(addres, contacts):
#     tmp1 = []
#     for i in range(len(contacts) - 1):
#         tmp = contacts[i]
#         if tmp.find(addres) > -1:
#             tmp1.append(contacts[i])
#         # print(tmp1)
#     return tmp1

def find_cont(to_find, contacts):            # Получает контакт(список контактов) по совпадениям имени, фамилии,
    tmp1 = []                                # Отчевтва, ФИО, адреса или номера телефона
    try:                                     # Блок try для того, чтобы конвертировать to_find в int тк числа при поиске имеют               
        to_find = int(to_find)               # тип str. И без этого блока не работает поиск с числом 4 (5 работает)
    except:
        to_find
    if type(to_find) == int:                                                            
        for i in range(len(contacts)):
            tmp = contacts[i].split()
            if to_find == int(tmp[-1]):
                tmp1 = contacts[i]
    else:
        to_find = to_find.strip().lower()                     # Регистр запроса не имеет значения
        for i in range(len(contacts)):
            tmp = contacts[i].lower()
            j = tmp.find(to_find)
            
            if i > -1 and tmp[j + len(to_find)] != " ":       # Если искомая строка содержится в справочнике
                tmp = tmp[:j] + tmp[j + 1:]                   # И после строки пробел(чтобы исключить              
            j = tmp.find(to_find)                             # выдачу "Антонов" при поиске "Антон")
            if j > -1 and tmp[j + len(to_find)] == " ":    
                tmp1.append(contacts[i])
    return tmp1


def put_cont(file_name, data):                        # Добавляет в словарь новую запись
    with codecs.open(file_name, 'a', "utf_8") as f:           
        str_dir = "\n" + data
        f.write(str_dir)


def import_directory(directory):
    with codecs.open( directory, "r", "utf_8" ) as f:
        contacts = f.read().split('\n')
    return contacts

def export_directory(new_directory, file):
    with codecs.open(new_directory, 'a', "utf_8") as f:
        for i in range(len(file)):
            f.write(file[i] +'\n')
        



