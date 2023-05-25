def list_deepcopy(L):
    result = []

    def items_generator(lst):
        yield from lst

    gens = [(items_generator(L), result)]
    while len(gens) > 0:
        gen_struct = gens.pop()

        gen = gen_struct[0]
        items = gen_struct[1]
        for item in gen:
            if isinstance(item, list):
                child = []
                gens.append((items_generator(item), child))
            else:
                child = item
            items.append(child)

    return result

L2 = list_deepcopy(L1)




 