def get_next_multiple(nums):
    for num in nums:
        yield num + num
        yield num + num + num
        yield num + num + num + num
        yield num + num + num + num + num
        yield num + num + num + num + num + num


numbers = [13]
gen_multiple_of_two = get_next_multiple(numbers)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
