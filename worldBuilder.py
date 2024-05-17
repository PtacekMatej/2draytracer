def build(size):
    world = [0] * size * size
    for i in range(size):
        world[i] = 1
        world[-i] = 1
        world[size * i] = 1
        world[size * i - 1] = 1

    for i in filter(lambda x: x % 14 == 0, range(size*size)):
        world[i] = 1
    
    return world