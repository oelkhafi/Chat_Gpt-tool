from collections import namedtuple
from collections import defaultdict

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

def collect_statistics(statistics):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            food, count = args
            response_code, max_count = func(*args, **kwargs)
            portions = max_count if response_code else count - max_count
            statistics[food].append(Order(response_code, portions))
            return response_code, max_count

        return inner

    return decorator


def get_max_portions(food, recipes, store):
    portions = []
    for ingredient, count in recipes[food].items():
        portions.append(store.get(ingredient, 0) // count)
    return min(portions)


@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    max_portions = get_max_portions(food, recipes, store)
    if max_portions < count:
        return 0, max_portions
    return 1, count 