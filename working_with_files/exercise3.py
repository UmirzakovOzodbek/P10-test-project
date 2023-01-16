def count_lines():
    count_lis = list()
    try:
        file = open("story.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.readlines()
        for index in res:
            if not index[0] == "T":
                count_lis.append(index)

        file.close()
        return len(count_lis)


print(count_lines())