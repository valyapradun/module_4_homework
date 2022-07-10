from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
    which splits the `s` string by indexes specified in `indexes`. Wrong indexes
    must be ignored.
    """
    result = []
    start = 0
    for i in indexes:
        if i > len(s):
            result.append(s[start:len(s)])
            break
        else:
            result.append(s[start:i])
            start = i
            if i == indexes[-1]: result.append(s[start:len(s)])
    return result


if __name__ == '__main__':
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
    print(split_by_index("no luck", [42]))
