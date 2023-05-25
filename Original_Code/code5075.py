import sys


def emit(key: tuple, value: int) -> None:
    word, docname = key
    print(f""{word}\t{docname}\t{value}"")


def _reduce(counter: dict) -> None:
    for key, value in counter.items():
        emit(key, value)


def main():
    counter = {}
    for line in sys.stdin:
        word_doc, n = line.split(""\t"")
        key, value = tuple(word_doc.split(""#"")), int(n)
        
        counter[key] = counter.get(key, 0) + value
    
    _reduce(counter)

if __name__ == ""__main__"":
    main()
 