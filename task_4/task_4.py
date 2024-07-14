from utils import *


def main():
    phone_book = {}
    try:
        while True:
            user_input = input('Enter command: ').strip()
            if user_input:
                command, *args = parse_input(user_input)

                match command:
                    # Finish
                    case 'exit' | 'close':
                        print(bot_answer('Goodbye!'))
                        break

                    # Greeting
                    case 'hi' | 'hello':
                        print(bot_answer('Hello! How can I help you?'))

                    # Add contact
                    case 'add':
                        print(add_contact(phone_book, *args))

                    # Change contact
                    case 'change':
                        print(change_contact(phone_book, *args))

                    # Show contact
                    case 'phone':
                        print(show_contact(phone_book, *args))

                    # Show all contact
                    case 'all':
                        print(show_all(phone_book))

                    # Show info
                    case 'info':
                        print(show_info())

                    # Invalid command
                    case _:
                        print(bot_answer('I don\'t know how to handle this command.'))

    except KeyboardInterrupt:
        print(bot_answer('Oops.. Something went wrong..'))


if __name__ == '__main__':
    main()
