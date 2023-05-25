from itertools import cycle


def disc_generator(alphabet):
    l = list(alphabet)
    random.shuffle(l)
    return """".join(l)


discs = [disc_generator(clear_alphabet) for i in range(n)]


def lcaesar(letter, key, alphabet=""ABCDEFGHIJKLMNOPQRSTUVWXYZ""):
    return alphabet[(alphabet.index(letter) + key) % len(alphabet)]


def jefferson_encryption(text, discs, step, reverse=False):
    key = -step if reverse else step
    return """".join(
        lcaesar(letter, key, disc)
        for letter, disc in zip(
            filter(clear_alphabet.__contains__, text.upper()), cycle(discs)
        )
    )
 