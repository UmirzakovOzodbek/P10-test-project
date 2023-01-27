def even_number_filter(number):
    return number % 2 == 0


def only_even_parameters(func):
    def even_inner(*args):
        if len(args) == len([num for num in filter(even_number_filter, args)]):
            return func(*args)
        else:
            return "Please add only even numbers!"

    return even_inner


@only_even_parameters
def add(a, b):
    return a + b


print(add(6, 8))
print(add(1, 4))





