import model
import view

def import_dir():
    directory = view.import_dir()
    contacts = model.import_directory(directory)
    return contacts

def print_directory():
    contacts = import_dir()
    view.print_contacts(contacts)

def find_contact():
    contacts = import_dir()
    find = view.find_contact()
    cont = model.find_cont(find, contacts)
    view.print_contacts(cont)

def put_contact():
    l = view.put_contact()
    model.put_cont(l[0], l[1])

def export():
    contacts = import_dir()
    file = view.export()
    model.export_directory(file, contacts)
