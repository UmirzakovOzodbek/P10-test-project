def get_next_prime():
    for i in range(1, 1000):
        prime = [x for x in range(1, i + 1) if i % x == 0]
        if len(prime) == 2:
            yield i


iterator = get_next_prime()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
