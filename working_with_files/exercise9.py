def main_action(str_):
    char = '#'
    str_ += char
    return str_


def count_uppercase():
    res = ''
    try:
        file = open('matter.txt', 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
    else:
        for i in file.read():
            res += main_action(i)

        # [res + main_action(i) for i in file.read()]
    # res += main_action("a")
    return res


print(count_uppercase())