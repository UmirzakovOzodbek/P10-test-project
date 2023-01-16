def counter(str_, char):
    res = str_
    return res.count(char)


def AMcount():
    a_count = 0
    m_count = 0
    try:
        file = open('STORY.txt', 'r', encoding='utf-8')

    except FileNotFoundError as e:
        print("x")
    else:
        for i in file.read():
            if i == "a":
                a_count += 1
            elif i == "m":
                m_count += 1
        res = f'A or a : {a_count}\n' \
              f'M or m : {m_count}'
        return res


print(AMcount())