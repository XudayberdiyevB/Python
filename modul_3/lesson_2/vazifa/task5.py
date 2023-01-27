"""
sum_index nomli funksiya yarating va bu funksiya faqat list qabul qilsin. Funksiya berilgan list indexlari
yig'indisini qaytarsin. Funksiyaga beriladigan argumentni tekshirish uchun dekorator yozing.
"""


def get_type(func):
    def get_check_type(list_):
        if type(list_) != list:
            return f"Please send only list."
        else:
            return func(list_)

    return get_check_type


@get_type
def sum_index(list_):
    sum_ = 0
    for i in enumerate(list_):
        sum_ += i[0]
    return sum_


lst_ = [1, 3, 5, 3, 4]
print(sum_index(lst_))
