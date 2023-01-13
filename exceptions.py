def write_exception(error):
    with open("exceptions.txt", "a") as f:
        f.write(f"{error}\n")
