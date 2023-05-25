import sys
import re

def emit(key: tuple, value: int) -> None:
    word, docname = key
    print(f""{word}#{docname}\t{value}"")


def _map(docname: str, content: str) -> None:
    for word in content:
        word = word.strip()
        if word:
            emit((word, docname), 1)


def main():
    for line in sys.stdin:
        docname, value = line.rstrip().split("":"", 1)
        value = re.sub(r""[\W_]"", "" "", value)
        _map(docname, value.split("" ""))


if __name__ == ""__main__"":
    main() 