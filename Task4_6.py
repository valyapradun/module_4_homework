def get_longest_word(s: str) -> str:
    """
    Implement a function `get_longest_word(s: str) -> str` which returns the
    longest word in the given string. The word can contain any symbols except
    whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
    the string with a same length return the word that occures first.
    """
    all_words = s.split()
    max_length = ''
    for word in all_words:
        if len(word) > len(max_length):
            max_length = word

    return max_length


if __name__ == '__main__':
    print(get_longest_word('Python is simple and effective!'))
    print(get_longest_word('Any pythonista like namespaces a lot.'))
