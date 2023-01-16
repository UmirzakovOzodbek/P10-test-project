def count_lines():
    result = list()
    try:
        file = open("define_e.txt", "r", encoding='utf-8')
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read().lower().split()
        for word in res:
            if word[-1] == "e":
                result.append(word)
        print(res)
        file.close()
        print(f"\nNumber of ending with alphabet 'e': {len(result)}")
        return result


print(count_lines())