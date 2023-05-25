from collections import OrderedDict, Callable
from numpy import mean


class DefaultOrderedDict(OrderedDict):
    def __init__(self, default_factory=None, *a, **kw):
        if (default_factory is not None and
                not isinstance(default_factory, Callable)):
            raise TypeError('first argument must be callable')
        OrderedDict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value


def fill_mapper():
    _mapper = DefaultOrderedDict(list)
    while True:
        try:
            data = input()
            website, time = data.split()
            _mapper[website].append(int(time))
        except EOFError:
            break
    return _mapper


def print_result(_mapper):
    for website, time in _mapper.items():
        print('{}\t{}'.format(website, int(mean(time))))


mapper = fill_mapper()
print_result(mapper) 