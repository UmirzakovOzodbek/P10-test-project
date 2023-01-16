def JTOI():
    res = list()
    result = None
    try:
        file = open('WORDS.txt', 'r', encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
    else:
        result = file.read().replace("J", "I")
    return result


print(JTOI())