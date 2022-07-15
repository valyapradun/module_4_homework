from typing import List


def foo(input_list: List[int]) -> List[int]:
    """
    Implement a function `foo(List[int]) -> List[int]` which, given a list of
    integers, return a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array except the one at `i`.
    """
    result = []
    multiplication_all = 1
    for i in input_list:
        multiplication_all *= i

    for i in input_list:
        result.append(multiplication_all // i)

    return result


if __name__ == '__main__':
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
