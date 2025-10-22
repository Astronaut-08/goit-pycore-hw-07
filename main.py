'''Наш головний бот'''

from adressbook import AddressBook
from bot_functions import parse_input, add_contact, change_contact, get_user_phone
from bot_functions import add_birthday, show_birthday, birthdays

def main():
    '''Main programm'''
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(get_user_phone(args, book))

        elif command == "all":
            for user in book.data.values():
                print(user)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            for user, congrat_date in birthdays(book):
                print(f'{user} | congrat_date: {congrat_date}')

        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
