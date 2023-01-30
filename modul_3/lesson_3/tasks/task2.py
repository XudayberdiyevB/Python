"""
test.txt faylda so'zlar berilgan ushbu so'zlardagi har bir harfni
 generator funksiya orqali oling.
"""
from Python.python_exceptions import write_exceptions


def get_open_file():
    try:
        with open("test.txt") as files:
            file = files.read()

    except FileNotFoundError as e:
        write_exceptions(e)
    return file


def generator():
    info = get_open_file()
    for i in info:
        yield i


generator_1 = generator()
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
