"""
get_next_prime generator funksiya yarating,bunda 1 dan 1000
 gacha sonlar orasida tub sonlarni next() orqali olish mumkin bo'lsin.
"""


def get_next_prime():
    for i in range(1, 1000):
        c = [x for x in range(1, i + 1) if i % x == 0]
        if len(c) == 2:
            yield i


prime = iter(get_next_prime())
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
