def build(size):
    world = [0] * size * size
    for i in range(size):
        world[i] = 1
        world[-i] = 1
        world[size * i] = 1
        world[size * i - 1] = 1

    for i in filter(lambda x: ((x % 16 == 0 or (x // size) % 16 == 0) and not (x % 16 == 8 or (x // size) % 16 == 8)) or (x % 16 == 8 and (x // size) % 16 == 8) , range(size*size)):
        world[i] = 1
    
    return world