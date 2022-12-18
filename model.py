
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

def get_cont(to_find, contacts):                            # Получает контакт(список контактов) по совпадениям имени, фамилии,
    tmp1 = []                                               # Отчевтва, ФИО, адреса или номера телефона
    if type(to_find) == str:
        to_find = to_find.strip().lower()
        for i in range(len(contacts)):
            tmp = contacts[i].lower()
            if tmp.find(to_find) > -1 and tmp[tmp.find(to_find) + len(to_find)] == " ":
                tmp1.append(contacts[i])
            # print(tmp1)
    elif type(to_find) == int:
        for i in range(len(contacts)):
            tmp = contacts[i].split()
            if to_find == int(tmp[-1]):
                tmp1 = contacts[i]
    return tmp1


def put_cont(name, phone, addres):
    return 0

def import_directory(directory):
    return 0

def export_directory(directory):
    return 0

