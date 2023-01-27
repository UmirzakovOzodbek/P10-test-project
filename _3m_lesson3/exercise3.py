def multiplication_two_number(func):
    def multiplication_inner(a, b):
        return f"({a} + {a}) + ({b} + {b}) = {(a + b) * 2}"

    return multiplication_inner


@multiplication_two_number
def decoration(a, b):
    return (a + b) * 2


print(decoration(2, 3))
print(decoration(5, 5))


