def add_even_number(a, b, c, d):
    def add_inner():
        if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
            return "Please add only even numbers!"
        else:
            return a + b + c + d

    return add_inner


add = add_even_number(6, 8, 2, 2)
add1 = add_even_number(1, 4, 2, 2)
print(add())
print(add1())


def multiply_even_number(a, b, c, d):
    def multiply_inner():
        if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
            return "Please multiply only even numbers!"
        else:
            return a * b * c * d

    return multiply_inner


add = add_even_number(6, 8, 2, 2)
add1 = add_even_number(1, 4, 2, 2)
print(add())
print(add1())






