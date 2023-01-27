def sum_index(type):
    def sum_inner(a, b, c, d):
        try:
            type([a, b, c, d])
        except TypeError:
            return "Please send only list!"

    return sum_inner


@sum_index
def sum_(a, b, c, d):
    for index in [a, b, c, d]:
        len(index)
    return sum(index)


print(sum_([2], [4], [5], [6]))
print(sum_(1, 2, 3, 4))



