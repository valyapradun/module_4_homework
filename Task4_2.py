import re


def check_palindrome(string: str = '') -> bool:
    """
    Write a function that check whether a string is a palindrome or not. Usage of
    any reversing functions is prohibited. To check your implementation you can use
    strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
    """
    string = re.sub('[ \t\n\x0b\r\f,&]', '', string).lower()
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string = reversed_string + string[i]

    if (string != '') & (string == reversed_string): return True
    else: return False


if __name__ == '__main__':
    print(check_palindrome(''))
    print(check_palindrome('abc'))
    print(check_palindrome('madam'))
    print(check_palindrome('ΝΙΨΟΝ ΑΝΟΜΗΜΑΤΑ ΜΗ ΜΟΝΑΝ ΟΨΙΝ'))
    print(check_palindrome('Lewd did I live, & evil I did dwel'))
