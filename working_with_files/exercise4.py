def count_display():
    try:
        file = open("notes.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read().lower()
        print(res)
        print(f"Number of the: {res.count('the')}")
        file.close()

        return ""


print(count_display())
