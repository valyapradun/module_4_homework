from typing import List


def imposter_split(self: str, sep: str = ' ') -> List[str]:
    """
    Implement a function which works the same as `str.split` method
    (without using `str.split` itself, ofcourse).
    """
    result = []
    start = 0
    while True:
        end = self.find(sep, start)
        if end == -1:
            result.append(self[start:len(self)])
            break
        else:
            result.append(self[start:end])
        start = end + len(sep)
    return result


if __name__ == '__main__':
    print(imposter_split('aaa aa aa', ' '))
    print(imposter_split('This  is  string  to  test', '  '))
    print(imposter_split('This* is* string* to* test', '* '))
