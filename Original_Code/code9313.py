def generate_parts(num: int):
    s = str(num ** 2)
    half = len(s) // 2

    yield s[:half], s[half:]

    last_index = 1
    left_half_len = len(s[:half])
    while last_index <= left_half_len:
        last_pos = half - last_index
        last_symbol = s[last_pos]
        if last_symbol != ""0"":
            break
        yield s[:last_pos], s[last_pos:]
        last_index += 1


def get_number(s: str):
    return int(s or ""0"")


def get_part_sum(part):
    return sum(get_number(item) for item in part)


def check_part(part, src):
    return get_number(part[-1]) != 0 and get_part_sum(part) == src


def kaprekar(n):
    for part in generate_parts(n):
        if check_part(part, n):
            return True
    return False
 