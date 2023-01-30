def gen_func():
    with open('test.txt', 'r') as f:
        yield f.read()


my_generator = gen_func()
print(next(my_generator))