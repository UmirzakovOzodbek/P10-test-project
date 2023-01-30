def gen_func():
    with open('planet.txt', 'r') as f:
        file = f.read()
    for char in file:
        if "name" in char:
            yield char.split("=")[1]


planets_gen = gen_func()
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))


