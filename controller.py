import model
import codecs


f = codecs.open( "directory.txt", "r", "utf_8_sig" )

contacts = f.read().split('\n')


# print(contacts)

# model.get_cont_full_name('asd','asf', 'asfasf,', contacts)
# print(model.get_cont_full_name('Сидоров','Пётр', 'Петрович', contacts))

# print(model.get_cont_part_name('Иванов', contacts))

# print(model.get_cont_phone(325568, contacts))

# print(model.get_cont_addres("Москва", contacts))

# print(model.get_cont(456321, contacts))

# print(model.get_cont('Иркутск', contacts))

model.put_cont("directory.txt", "Семёнов Иван Семёнович", "Великий Новгород", 3456333)


f.close()