import sys
from math import inf


def _emit(key: str, value: tuple) -> None:
    dist, children = value
    dist = (""INF"" if dist == inf else int(dist))
    children = ""{"" + "","".join(children) + ""}""
    print(f""{key}\t{dist}\t{children}"")


def _reduce(key: str, values: list) -> None:
    min_dist, _ = min(values, key=lambda v: v[0])
    _, children = max(values, key=lambda v: len(v[1]))
    _emit(key, (min_dist, children))


def main():
    d = {}
    for line in sys.stdin:
        key, dist, children = line.rstrip().split(""\t"")
        children = tuple(filter(lambda v: v, children.strip(""{}"").split("","")))
  
        d.setdefault(key, []).append((float(dist), children))

    for key, values in d.items():
        _reduce(key, values)


if __name__ == ""__main__"":
    main()
 