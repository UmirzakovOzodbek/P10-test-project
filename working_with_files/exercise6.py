def write_exception(exception, e):
    with open("new_exceptions.txt", "a") as file:
        dct = {exception: e}
        file.write(f"{dct}\n")


def display_words():
    try:
        file = open("articles.txt", "r", encoding='utf-8')
    except Exception as e:
        write_exception(Exception, e)
    else:
        words = list()
        [words.append(word) for word in file.read().lower().split() if word == "this" or word == "these"]
        print(file.read())
        return len(words)


print(display_words())
