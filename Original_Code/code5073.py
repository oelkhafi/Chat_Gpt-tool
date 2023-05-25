import sys


def emit(key: str, a: str, b: str) -> None:
    print(f""{key}\t{a}\t{b}"")


def _reduce(join_key: str, tagged_values: dict) -> None:
    values_iter = iter(tagged_values.items())
    _, a_values = next(values_iter)
    _, b_values = next(values_iter)
    
    for a in a_values:
        for b in b_values:
            emit(join_key, a, b)


def main():
    mapper = {}
    for line in sys.stdin:
        join_key, values = line.rstrip().split(""\t"")
        tag, value = values.split("":"")
        
        mapper.setdefault(join_key, {}).setdefault(tag, []).append(value)
    
    for join_key, tagged_values in mapper.items():
        if len(tagged_values) == 2: # only inner join supported for now
            _reduce(join_key, tagged_values)
        

if __name__ == ""__main__"":
    main()
 