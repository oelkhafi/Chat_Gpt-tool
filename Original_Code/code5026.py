def list_pull(L):
    result = []

    def pull_generator(lst):
        yield from lst

    gens = [pull_generator(L)]
    while len(gens) > 0:
        gen = gens.pop()
        for item in gen:
            if isinstance(item, list):
                gens.append(pull_generator(item))
            else:
                result.append(item)

    return result


L2 = list_pull(L1)




 