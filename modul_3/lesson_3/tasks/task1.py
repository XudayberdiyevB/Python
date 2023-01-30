"""
1 dan 20 gacha sonlarni toq bo'lsa o'zi, juft bo'lsa (-) operator qo'ygan holda
a. iterator
b. generator funksiya
orqali chiqaring.
"""


def func():
    for i in range(1, 21):
        if i % 2 == 0:
            yield f"-{i}"
        else:
            yield i


itr = iter(func())

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
