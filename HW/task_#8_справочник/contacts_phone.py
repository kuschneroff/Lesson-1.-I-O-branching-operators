def show_data(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")

def add_contact(contacts):
    fio = input("Введите ФИО: ")
    phone_number = input("Введите номер телефона: ")
    street_name = input('Введите адрес: ')
    comment = input('Введите комментарий: ')
    contact = {'id': len(contacts) + 1, 'name': fio, 'phone': phone_number, 'adress': street_name, 'comment': comment}
    contacts.append(contact)
    print(f"Добавлена запись: {contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")

def edit_contact(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")
    index = int(input("Введите порядковый № контакта для редактирования: ")) - 1
    if index >= 0 and index < len(contacts):
        contact = contacts[index]
        fio = input("Введите измененные данные ФИО: ")
        phone = input("Введите измененный номер телефона: ")
        street_name = input("Введите измененный адрес: ")
        comment = input("Введите измененный комментарий: ")
        if fio:
            contact['name'] = fio
        if phone:
            contact['phone'] = phone
        if street_name:
            contact['adress'] = street_name
        if comment:
            contact['comment'] = comment
        print(f"Изменена запись №{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")
    else:
        print("Неправильный порядковый № контакта\n")

def delete_contact(contacts):
    print("\n№ | ФИО | Телефон | Адрес | Комментарий |")
    for contact in contacts:
        print(f"{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}")
    print("")
    index = int(input("Введите номер контакта для удаления: ")) - 1
    if index >= 0 and index < len(contacts):
        contact = contacts.pop(index)
        print(f"Удалена запись №{contact['id']} | {contact['name']} | {contact['phone']} | {contact['adress']} | {contact['comment']}\n")
    else:
        print("Неправильный порядковый № контакта\n")

def main():
    file_path = "contacts.txt"

    contacts = []

    while True:
        print("Выберите одно из действий:")
        print("1 - Чтение информации контакта")
        print("2 - Добавить контакт")
        print("3 - Редактировать контакт")
        print("4 - Удалить контакт")
        print("5 - Копировать данные из одного файла в другой")
        print("0 - Выход")
        action = input("Действие: ")
        if action == '1':
            show_data(contacts)
        elif action == '2':
            add_contact(contacts)
        elif action == '3':
            edit_contact(contacts)
        elif action == '4':
            delete_contact(contacts)
        elif action == '5':
            copy_data()
        elif action == '0':
            break
        else:
            print("Неправильный выбор\n")

    print("До свидания!  Good Bye! Aufwiedersehen! Hasta la vista! Arrivederci! 再见！")

def copy_data():
    source_file = input("Введите имя файла, из которого нужно скопировать данные: ")
    destination_file = input("Введите имя файла, в который нужно скопировать данные: ")
    line_number = int(input("Введите номер строки, которую необходимо скопировать: "))

    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()
            if line_number >= 1 and line_number <= len(lines):
                line = lines[line_number - 1]
                with open(destination_file, 'a') as destination:
                    destination.write(line)
                print(f"Данные из строки {line_number} файла {source_file} успешно скопированы в файл {destination_file}")
            else:
                print("Неправильный номер строки")
    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    main()

