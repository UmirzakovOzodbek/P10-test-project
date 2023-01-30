def gen_func():
    for i in range(1, 21):
        if i % 2 == 0:
            yield i * (-1)
        else:
            yield i


my_generator = gen_func()
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
