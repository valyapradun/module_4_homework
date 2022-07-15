def generate_squares(number: int) -> dict:
    """
    Implement a function that takes a number N as an argument and returns a dictionary,
    where the key is a n (n ∈ [1, N]) and the value is the square of n (n**2).
    """
    return {i: i**2 for i in range(1, number+1)}


if __name__ == '__main__':
    print(generate_squares(5))
    print(generate_squares(1))
