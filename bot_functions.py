'''Винесені в окремий файл функції нашого бота для кращої організації та читабельності'''

from adressbook import Record
# тут є оновлення, ми не офіційно домовляємся в цьому боті явно піднімати KeyError тільки
# в тому випадку коли користувача не існує, у всіх інших випадках при підніманні exeption
# ми передаємо йому стрічку чому саме ми його підіймаємо, а де ми не передаємо стрічку
# python сам передає її, як наприклад неможливість розпакувати *args, таким чином код чистіший
def input_error(func):
    '''Декоратор який обробляє помилки ValueError, KeyError, IndexError'''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
# Модифіковуємо наш перехоплювач помилок на більш сучасний
        except (ValueError, IndexError) as e:
            return str(e)
        except KeyError:
            return 'User doesn\'t exist'
    return inner

def parse_input(user_input):
    '''Ця функція обробляє введене користувачем значення'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@ input_error
def add_contact(args, book):
    '''Ця функція додає користувача в книгу'''
    name, phone, *_ = args
    name = name.capitalize()
    record = book.find(name)
    message = 'Contact update successful'
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = 'Contact add successful'
    if phone:
        record.add_phone(phone)
    return message

@ input_error
def change_contact(args, book):
    '''Ця функція змінює номер телефону користувача в книзі'''
    name, old_phone, new_phone, *_ = args
    name = name.capitalize()
    message = 'Contact changed successful'
    if name not in book.data: # тут потрібно явно перевірити, інакше не працюватиме
        raise KeyError
    book.data[name].edit_phone(old_phone, new_phone)
    return message

@ input_error
def get_user_phone(args, book):
    '''Ця функція витягує номер користувача з книги'''
    name, *_ = args
    name = name.capitalize()
    if name in book.data:
        return [p.value for p in book.data[name].phones]
    raise KeyError

@input_error
def add_birthday(args, book):
    '''Додає дату народження до користувача'''
    name, birthday, *_ = args
    name = name.capitalize()
    message = 'Birthday added successful'
    if name not in book.data:
        raise KeyError
    book.data[name].add_birthday(birthday)
    return message

@input_error
def show_birthday(args, book):
    '''Повертає дату народження конкретного користувача'''
    name, *_ = args
    name = name.capitalize()
    if book.data[name].birthday is None:
        return 'Birthday doesn\'t added'
    return book.data[name].birthday.value

@input_error
def birthdays(book) -> list[Record]:
    '''Повертає всі дні народження протягом наступного тижня'''
    return book.get_upcoming_birthdays()
