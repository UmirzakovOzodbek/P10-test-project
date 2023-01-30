def gen_func():
    with open('planet.txt', 'r') as f:
        text = f.read()
    for char in text:
        if "name" in char:
            yield char.split("=")[1]


planets_gen = gen_func()
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))


