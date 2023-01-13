from exceptions import write_exception


# xercise12_1
def create_file(filepath, author_name):
    counter = 0
    try:
        with open(filepath, "r") as file:
            data = file.readlines()
    except FileNotFoundError as e:
        write_exception(e)
    else:
        for line in data:
            for d in line.split(","):
                if d.strip() == author_name:
                    counter += 1
    return counter


book_data = """123, A, AA, 1000
126, D, AA, 1003
127, C, CC, 1004
"""

print(create_file("Book123.txt", "AA"))


