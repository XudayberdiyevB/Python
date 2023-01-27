my_list = range(1, 21)
print(type(my_list))
iterator = iter(my_list)
for i in iterator:
    print(next(iterator))
