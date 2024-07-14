from utils import *


def main():
    phone_book = {}
    try:
        while True:
            user_input = input('Enter command: ').strip()
            if user_input:
                command, *args = parse_input(user_input)

                # Finish
                if command in ['exit', 'close']:
                    print(bot_answer('Goodbye!'))
                    break

                # Greeting
                elif command in ['hi', 'hello']:
                    print(bot_answer('Hello! How can I help you?'))

                # Add contact
                elif command == 'add':
                    print(add_contact(phone_book, *args))

                # Change contact
                elif command == 'change':
                    print(change_contact(phone_book, *args))

                # Show contact
                elif command == 'phone':
                    print(show_contact(phone_book, *args))

                # Show all contact
                elif command == 'all':
                    print(show_all(phone_book))

                # Show info
                elif command == 'info':
                    print(show_info())

                # Invalid command
                else:
                    print(bot_answer('I don\'t know how to handle this command.'))

    except KeyboardInterrupt:
        print(bot_answer('Oops.. Something went wrong..'))


if __name__ == '__main__':
    main()
