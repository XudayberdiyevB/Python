"""
planets ushbu fayldagi ma'lumotlardan faqat name olish uchun generator yozing.
"""
from Python.python_exceptions import write_exceptions


def get_open_file():
    try:
        with open("planets.txt") as files:
            file = files.readlines()

    except FileNotFoundError as e:
        write_exceptions(e)
    return file


def get_name():
    info = get_open_file()
    for i in info:
        if "name" in i:
            yield i.split("=")[1][:-1]


generator = get_name()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
