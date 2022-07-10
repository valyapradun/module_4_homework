from typing import Tuple


def get_digits(num: int = None) -> Tuple[int]:
    """
    Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
    of a given integer's digits.
    """
    if num is not None: result = [int(i) for i in str(num)]
    else: result = []
    return tuple(result)


if __name__ == '__main__':
    print(get_digits(87178291199))
    print(get_digits())
