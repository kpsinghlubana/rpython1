
from sys import argv
from odo import odo
from toolz import partition

literals = [True, False, None]


def parse(s):
    """ Parse strings to booleans, integers, or strings

    >>> parse("true")
    True
    >>> parse("1")
    1
    >>> parse('";"')
    ';'
    """
    for l in literals:
        s = s.strip('"\'')
        if s.lower() == str(l).lower():
            return l
    if s.isdigit():
        return int(s)
    return s


def get_args_kwargs(argv):
    source, target = argv[1], argv[2]
    kwargs = dict((k.lstrip('-').replace('-', '_'), parse(v))
                  for k, v in partition(2, argv[3:]))
    return (source, target), kwargs


if __name__ == '__main__':
    args, kwargs = get_args_kwargs(argv)
    odo(*args, **kwargs)
