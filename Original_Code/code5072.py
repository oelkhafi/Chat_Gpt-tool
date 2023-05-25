import sys
from collections import namedtuple


Entry = namedtuple(""Entry"", [""timestamp"", ""user_id"", ""url""])


def emit(key: int, value: str) -> None:
    print(value)


def project(entry: Entry) -> str:
    return entry.url
    

def _map(key: int, entry: Entry) -> None:
    emit(key, project(entry))


def main():
    for row_key, row in enumerate(sys.stdin, start=1):
        row = row.strip()
        if row:
            _map(row_key, Entry(*row.split(""\t"")))


if __name__ == ""__main__"":
    main()
 