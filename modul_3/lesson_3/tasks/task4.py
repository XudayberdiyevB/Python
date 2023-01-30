"""
countries of the world.csv fayldagi raqamlar (,) bilan
yozilgan shu raqamlarni (.) bilan boshqa csv faylga yozing,
 bunda (,) ni (.) aylantirish uchun writer funksiyani decorator orqali ishlating.
"""
import csv
from Python.python_exceptions import write_exceptions


def get_open_file():
    lst = []
    try:
        with open("countries of the world.csv") as files:
            file = csv.reader(files)
            for i in file:
                lst.append(i)

    except FileNotFoundError as e:
        write_exceptions(e)
    return lst


def get_replace(func):
    def replace(info):
        lst_ = []
        for i in get_open_file():
            for j in range(len(i)):
                i[j] = i[j].replace(",", ".")
            lst_.append(i)
        return func(lst_)

    return replace


@get_replace
def write_new_file(info):
    try:
        with open("new.csv", "w") as files:
            file = csv.writer(files)
            file.writerows(info)

    except FileNotFoundError as e:
        write_exceptions(e)


write_new_file(get_open_file())
