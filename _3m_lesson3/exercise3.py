def multiplication_two_number(a, b):
    def multiplication_inner():
        return f"({a} + {a}) + ({b} + {b}) = {(a + a) + (b + b)}"

    return multiplication_inner


multiplication = multiplication_two_number(2, 3)
multiplication1 = multiplication_two_number(5, 5)
print(multiplication())
print(multiplication1())
