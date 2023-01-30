def gen_func():
    with open('planet.txt', 'r') as f:
        file = f.read()
    for i in file:
        if "name" in i:
            yield i.split("=")[1]


planets_gen = gen_func()
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))
print(next(planets_gen))


