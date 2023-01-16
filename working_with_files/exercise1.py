def read_function():
    try:
        open('poem.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    else:
        with open('poem.txt', 'r') as file:
            # print(file.read())
            return file.read()


print(read_function())
