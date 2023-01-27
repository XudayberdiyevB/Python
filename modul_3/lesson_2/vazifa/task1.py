"""
get_next_multiple nomli generator yarating, bunda generator funksiya bitta son qabul qiladi.
 Yaratilgan generator obyekt next() orqali olganda berilgan son keyingi bo'luvchilarini qaytarsin.
"""


def get_next_multiple(value):
    num = value
    while True:
        yield value
        value += num


gen = get_next_multiple(2)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

