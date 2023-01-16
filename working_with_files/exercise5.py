def display_words():
    try:
        file = open("story_text.txt", "r+")
    except FileNotFoundError as e:
        print(e)
    else:
        words = list()
        [words.append(word) for word in file.read().split() if len(word) < 4]
        return f"{words} \nNumber of words less than four: {len(words)}"


print(display_words())
