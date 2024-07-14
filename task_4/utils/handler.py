import re
from colorama import Fore, init

init(autoreset=True)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return bot_answer('Enter the argument for the command.')
        except KeyError:
            return bot_answer('There are no contacts with that name.')
        except ValueError:
            return bot_answer('Enter correct arguments.')

    return inner


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: phone number
    :return: normilized phone number (format: +380XXXXXXXXX)
    """

    # delete all symbols all characters except numbers and '+' from the number.
    normalized_number = re.sub(r'[^\d+]', '', phone_number)
    if len(normalized_number.removeprefix('+38')) == 10:
        if not normalized_number.startswith('+'):
            if not normalized_number.startswith('38'):
                normalized_number = '+38' + normalized_number
            else:
                normalized_number = '+' + normalized_number

        return normalized_number


def bot_answer(msg: str) -> str:
    """
    :param msg: bot message

    bot response to the user
    """
    return f"{Fore.BLUE}bot: {Fore.CYAN}{msg}"


@input_error
def add_contact(phone_book: dict[str: str], *args: str) -> str:
    """
    :param phone_book: dictionary with contacts info
    :param args: <name> <phone number>

    Add new contact to phone book
    """
    name = args[0].capitalize()
    phone = normalize_phone(args[1])

    if name in phone_book:
        return bot_answer(f'Contact with name "{name}" - already registered.\n'
                          f'If you want to change a contact, ask for "change <name> <new number>"')
    elif phone:
        phone_book.update({name: phone})
        return bot_answer('Contact added.')
    else:
        return bot_answer('Invalid phone number.')


@input_error
def change_contact(phone_book: dict[str: str], *args: str) -> str:
    """
    :param phone_book: dictionary with contacts info
    :param args: <name> <phone number>

    Update contact phone number
    """
    name = args[0].capitalize()
    phone = normalize_phone(args[1])
    if phone:
        phone_book[name] = phone
        return bot_answer('Contact updated.')
    else:
        return bot_answer('Invalid phone number.')


@input_error
def show_contact(phone_book: dict[str: str], *args: str) -> str:
    """
    :param phone_book: dictionary with contacts info
    :param args: <name>

    Show contact info
    """
    name = args[0].capitalize()
    return bot_answer(f"{name}: {phone_book[name]}")


def show_all(phone_book: dict[str: str]) -> str:
    """
    :param phone_book: dictionary with contacts info

    Show all contacts info
    """
    phone_book_list = list()
    for key, item in phone_book.items():
        phone_book_list.append(bot_answer(f"{key}: {item}"))

    return '\n'.join(phone_book_list)


def show_info() -> str:
    """
    Show info about bot commands
    """
    return bot_answer('You can:\n'
                      '\t[1] add a new contact: add <name> <phone>;\n'
                      '\t[2] change a contact: change <name> <new phone>;\n'
                      '\t[3] get a number: phone <name>;\n'
                      '\t[4] get all contacts: all;\n')
