"""
Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing, bunda funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin
"""


def get_two_sum(func_):
    def get_num(a, b):
        return func_(a, b) * 2

    return get_num


@get_two_sum
def add(a, b):
    return a + b


func = add(2, 4)
print(func)
