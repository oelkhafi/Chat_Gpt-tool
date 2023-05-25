import sys


def emit(key: str, value: tuple) -> None:
    docname, tf, idf = value
    print(f""{key}\t{docname};{tf};{idf}"")


def _map(key: str, value: tuple) -> None:
    emit(key, (*value, 1))


def main():
    for line in sys.stdin:
        word, docname, tf = line.rstrip().split(""\t"")
        
        _map(word, (docname, tf))


if __name__ == ""__main__"":
    main()
 