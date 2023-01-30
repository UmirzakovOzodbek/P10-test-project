import csv


def get_csv():
    res = []
    try:
        with open("countries of the world.csv", "r", encoding="utf8") as f:
            read_file = csv.reader(f)
            for i in read_file:
                res.append(i)
    except FileNotFoundError as e:
        print(e)
    return res


def substitution(func):
    def replace(value):
        lst = []
        for i in get_csv():
            for j in range(len(i)):
                i[j] = i[j].replace(",", ".")
            lst.append(i)
        return func(lst)

    return replace


@substitution
def new_file_info(value):
    try:
        with open("country of the world2.csv", "w", encoding="utf8") as f:
            read_file = csv.writer(f)
            read_file.writerows(value)
    except FileNotFoundError as e:
        print(e)


print(substitution(new_file_info(get_csv())))

