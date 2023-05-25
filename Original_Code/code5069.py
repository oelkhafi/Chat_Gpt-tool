import sys


def emit(key: str, value: str) -> None:
    print(key)

    
def _reduce(key: str, array: list) -> None:
    if len(array) == 2:
        emit(key, None)


def main():
    d = {}
    for line in sys.stdin:
        key, value = line.strip().split(""\t"")
        d.setdefault(key, []).append(value)

    [_reduce(key, array) for key, array in d.items()]


if __name__ == ""__main__"":
    main()
 