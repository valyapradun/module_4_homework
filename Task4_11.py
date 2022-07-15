from collections import defaultdict


def combine_dicts(*args):
    """
    Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
    and combines them into one dictionary.
    Dict values should be summarized in case of identical keys
    """
    default = defaultdict(lambda: 0)
    for d in args:
        for key in d:
            default[key] = default[key] + d[key]

    return default


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))

