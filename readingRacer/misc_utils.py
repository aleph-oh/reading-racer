from collections import defaultdict


def invert_dict(d):
    """
    Inverts a dictionary mapping keys to non-nested iterable values

    :param d: dictionary mapping non-iterable keys to values which are iterables of
              non-iterables
    :type d: dict
    :return: dictionary mapping all non-iterables contained in iterables in values to a set of
             the keys corresponding to them
    :rtype: dict
    :raises TypeError: if d maps keys to strings or iterable non-string keys to any values
    """
    inverted = defaultdict(set)
    for k, iterable in d.items():
        if isinstance(iterable, str):
            raise TypeError("Mapping keys to strings not supported")
        if not isinstance(k, str) and hasattr(k, "__iter__"):
            raise TypeError("Mapping iterable non-string keys to values not supported")
        for v in iterable:
            inverted[v].add(k)
    return inverted
