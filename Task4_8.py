from typing import List
from typing import Tuple


def get_pairs(lst: List) -> List[Tuple]:
    """
    Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
    of tuples containing pairs of elements. Pairs should be formed as in the
    example. If there is only one element in the list return `None` instead.
    """
    if len(lst) > 1:
        return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]


if __name__ == '__main__':
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
    print(get_pairs([1]))
