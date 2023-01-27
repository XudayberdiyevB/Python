"""
Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing, bunda funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin
"""


def get_two_sum(num_1, num_2):
    sum_ = num_1 + num_2

    def get_num():
        return sum_ * 2

    return get_num


func = get_two_sum(5, 2)
print(func())
