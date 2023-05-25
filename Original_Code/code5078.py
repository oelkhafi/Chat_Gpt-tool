import sys


def _emit(key: str, value: list) -> None:
    key_dist = value[0]
    children = value[1]
    print(f""{key}\t{key_dist}\t{children}"")

    
def _incr_dist(dist: str):
    if dist == ""INF"":
        incr_dist = ""INF""
    else:
        incr_dist = int(dist) + 1
    return incr_dist


def _map(key: str, value: list) -> None:
    _emit(key, value)
    
    parent_dist = value[0]
    children = value[1]
    for child in children.strip(""{}"").split("",""):
        if child:
            _emit(child, [_incr_dist(parent_dist), {}])
        

def main():
    for line in sys.stdin:
        key, dist, children = line.rstrip().split(""\t"")
        _map(key, [dist, children])


if __name__ == ""__main__"":
    main() 