''''Задача 38: Дополнить телефонный справочник возможностью
изменения и удаления данных. Пользователь также может ввести
имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных

*доработать справочник в модульном варианте
'''''

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

def search_contacts(contacts):
    keyword = input("Введите ключевое слово для поиска: ")
    search_results = []
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or \
                keyword.lower() in contact['phone'].lower() or \
                keyword.lower() in contact['adress'].lower() or \
                keyword.lower() in contact['comment'].lower():
            search_results.append(contact)
    if search_results:
        print("Результаты поиска:")
        show_data(search_results)
    else:
        print("Контакты не найдены.")

def sort_contacts(contacts):
    print("Выберите поле для сортировки:")
    print("1 - Имя")
    print("2 - Номер телефона")
    print("3 - Адрес")
    print("4 - Комментарий")
    option = input("Действие: ")
    if option == '1':
        sorted_contacts = sorted(contacts, key=lambda x: x['name'])
    elif option == '2':
        sorted_contacts = sorted(contacts, key=lambda x: x['phone'])
    elif option == '3':
        sorted_contacts = sorted(contacts, key=lambda x: x['adress'])
    elif option == '4':
        sorted_contacts = sorted(contacts, key=lambda x: x['comment'])
    else:
        print("Неправильный выбор.")
        return
    print("Контакты отсортированы:")
    show_data(sorted_contacts)

def main():
    contacts = []

    while True:
        print("Выберите одно из действий:")
        print("1 - Чтение информации контакта")
        print("2 - Добавить контакт")
        print("3 - Редактировать контакт")
        print("4 - Удалить контакт")
        print("5 - Поиск контактов")
        print("6 - Сортировка контактов")
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
            search_contacts(contacts)
        elif action == '6':
            sort_contacts(contacts)
        elif action == '0':
            break
        else:
            print("Неправильный выбор\n")

    print("До свидания!  Good Bye! Aufwiedersehen! Hasta la vista! Arrivederci! 再见！")

if __name__ == "__main__":
    main()