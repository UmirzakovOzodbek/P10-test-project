def sum_index(class_):
    def sum_inner(number):
        if type(class_) == list:
            for i in range(len(number)):
                return sum(number)
        else:
            return "Please send only list!"

    return sum_inner


sum1 = sum_index([2, 4, 5, 6])
sum2 = sum_index((2, 4, 5, 6))
print(sum1([2, 4, 5, 6]))
print(sum2((2, 4, 5, 6)))







