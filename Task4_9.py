import string
from collections import defaultdict


def all_strings(*args):
    """
    Implement a functions which receive a changeable number of strings and return
    characters that appear in all strings
    """
    return sorted(set.intersection(*map(set, args)))


def least_one(*args):
    """
    Implement a functions which receive a changeable number of strings and return
    characters that appear in at least one string
    """
    return sorted(set.union(*map(set, args)))


def least_two(*args):
    """
    Implement a functions which receive a changeable number of strings and return
    characters that appear in at least in two strings
    """
    default = defaultdict(lambda: 0)
    for s in args:
        set_str = set(s)
        for character in set_str:
            default[character] = default[character] + 1

    res = [key for key in default if default[key] >= 2]
    return res


def not_any(*args):
    """
    Implement a functions which receive a changeable number of strings and return
    characters of alphabet, that were not used in any string
    Note: use `string.ascii_lowercase` for list of alphabet letters
    """
    list_one = sorted(set.union(*map(set, args)))
    alphabet = sorted(set(string.ascii_lowercase))
    return [i for i in alphabet if i not in list_one]


if __name__ == '__main__':
    test_strings = ["hello", "world", "python", ]
    print(all_strings(*test_strings))
    print(least_one(*test_strings))
    print(least_two(*test_strings))
    print(not_any(*test_strings))
