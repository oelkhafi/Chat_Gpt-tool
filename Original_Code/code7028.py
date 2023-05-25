from random import randint


def rabin_karp(pattern, text):
    prime = 100000007
    factor = randint(1, prime-1)
    npat = len(pattern) - 1

    pat_hash = sum(ord(pattern[i]) * pow(factor, npat - i, prime) % prime
                   for i in range(npat + 1)) % prime
    cur_hash = sum(ord(text[i]) * pow(factor, npat - i, prime) % prime
                   for i in range(npat + 1)) % prime
    hi_factor = pow(factor, npat, prime)
    indexes = []

    if cur_hash == pat_hash and text[:npat+1] == pattern:
        indexes.append(0)

    for i in range(1, len(text) - npat):
        cur_hash = ((cur_hash - ord(text[i-1]) * hi_factor) * factor
                    + ord(text[i+npat])) % prime
        if cur_hash == pat_hash and text[i: i+npat+1] == pattern:
            indexes.append(i)

    return indexes


def test():
    assert rabin_karp(""aba"", ""abacaba"") == [0, 4]
    assert rabin_karp(""Test"", ""testTesttesT"") == [4]
    assert rabin_karp(""aaaaa"", ""baaaaaaa"") == [1, 2, 3]
    print(""OK"")


def main():
    print(*rabin_karp(input(), input()))


if __name__ == ""__main__"":
    main()
 