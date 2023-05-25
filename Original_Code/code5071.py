import sys
from collections import namedtuple


Entry = namedtuple(""Entry"", [""timestamp"", ""user_id"", ""url""])
predicate = lambda user_id: user_id == ""user10""


def emit(key: int, value: Entry) -> None:
    print(""\t"".join(value))


def _map(key: int, value: Entry) -> None:
    if predicate(value.user_id):
        emit(key, value)


def main():
    for row_key, row in enumerate(sys.stdin, start=1):
        row = row.strip()
        if row:
            _map(row_key, Entry(*row.split(""\t"")))


if __name__ == ""__main__"":
    main()
 