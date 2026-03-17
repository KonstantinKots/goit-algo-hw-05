
'''
Бот для роботи з контактаними данними та календарем.
Збереження/додавання/вивід в консоль контактів, знаходження телефону за ім'ям.

{"name": "phone"}

1. створити словник контактів та додати в нього інформацію
2. написати функцію яка буде дадавати новий контакт
3. написати функцію яка буде перезаписувати існуючий контакт
3. написати функцію яка буде виводити необхідний контакт
4. написати функцію яка буде виводити всі контакти
5. написати цикл який буде отримувати інформацію від користувача та реагувати на неї
'''
con_file = "contact.txt"

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me correct name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

#функція парсингу командної сторки
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: list, contacts: dict):
    """Додає новий контакт у словник contacts.
    
    args: список [ім'я, номер телефону]
    contacts: словник існуючих контактів
    Повертає повідомлення про успішне додавання.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict):
    """Оновлює телефон існуючого контакту у словнику contacts.
    
    args: список [ім'я, номер телефону]
    contacts: словник існуючих контактів
    Повертає повідомлення про успішну зміну.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error    
def show_phone(args: list, contacts: dict):
    """Пошук телефону за ім'ям у словнику contacts.
    
    args: список [ім'я, номер телефону]
    contacts: словник існуючих контактів
    Повертає повідомлення (ім'я):(телефон).
    """
    name = args[0].strip()
    if name not in contacts:
        raise KeyError
    return (f"{name}:{contacts[name]}")

def show_all(contacts: dict):
    """Виводить всі контакти зі словника contacts.
    
    contacts: словник існуючих контактів
    Повертає повідомлення (ім'я):(телефон).
    """
    result = ""
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result.strip()

def save_contacts(contacts: dict):
    """Записує словник contacts у текстовий файл.
    
    contacts: словник існуючих контактів
    """
    with open(con_file, 'w', encoding='utf-8') as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

def read_contact_file():
    """Зчитує контактні данні з текстового файлу.

    Очукваний формат формат кожного рядка name:phone    
    Повертає словник у форматі {name}:{phone}.
    За відсутності файлу повертає порожній словник
    """
    contacts = {}
    try:
        with open(con_file, 'r', encoding='utf-8') as file:
            for line in file:
                if ":" in line:
                    name, phone = line.strip().split(":", 1)
                    contacts[name.strip()] = phone.strip()
    except FileNotFoundError:
        return {}
    return contacts

#Головний цикл бота. Очікує введення команди користувачем та виконує їх
def main():
    contacts = read_contact_file()
    commands = '''
1) exit, close - to exit the application
2) add [name] [new phone] - to add a new contact
3) change [name] [new phone] - to change the contact
4) phone [name] - to print number phone
5) all - to print all numbers
6) help - to print this menu
'''
    print("\nWelcome to the assistant bot!\n")
    print(commands)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_contacts(contacts)
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "help":
            print(commands)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
