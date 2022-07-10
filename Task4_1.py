def change_quotes(string: str = '') -> str:
    """
    Implement a function which receives a string and replaces all `"` symbols
    with `'` and vise versa.
    """
    for i in string:
        if i == '"':
            string = string.replace(i, "'", 1)
        elif i == "'":
            string = string.replace(i, '"', 1)
    return string


if __name__ == '__main__':
    print(change_quotes())
    print(change_quotes("This string contains single quotes: ' and '."))
    print(change_quotes('This string contains double quotes: " and ".'))
    print(change_quotes('This string contains two types quoters: ", " and \', \' .'))
