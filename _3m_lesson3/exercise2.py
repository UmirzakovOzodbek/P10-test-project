def get_next_prime():
    for i in range(1, 1001, 2):
        yield i


s = get_next_prime()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


# def get_next_prime():
#     numbers = range(1, 1001, 2)
#     iterator = iter(numbers)
#
#     for _ in numbers:
#         return iterator
#
#
# number = get_next_prime()
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))


