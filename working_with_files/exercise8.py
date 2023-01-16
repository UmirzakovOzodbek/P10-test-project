def count_uppercase():
    res = list()
    try:
        file = open('text.txt', 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
    else:
        [res.append(i) for i in file.read() if i.isupper()]
        print(f"Number of Uppercase Letters: {len(res)}")
        return res


print(count_uppercase())