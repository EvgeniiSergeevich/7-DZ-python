import model
import view

directory = view.import_dir()
contacts = model.import_directory(directory)
# def print_directory():
#     view.print_contacts(contacts)

def find_contact():
    find = view.find_contact()
    cont = model.find_cont(find, contacts)
    view.print_contacts(cont)

# l = view.put_contact()
# model.put_cont(l[0], l[1])


# model.export_directory('123.csv', contacts)

