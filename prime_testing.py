import sys


def test_if_prime(x):
    """ Naive function that tests if any number from 2 to sqrt(x) is a divisor of x. If not, x is prime.
    """
    sqrt = int(n**0.5) + 1
    for i in range(2, sqrt):
        if x % i == 0:
            return False
    return True


def first_prime_bigger_than(start_n):
    """ Returns the first prime number bigger than or equal to n.
    """
    if start_n % 2 == 0:
        start_n += 1
    while not test_if_prime(start_n):
        start_n += 2
    return start_n


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("I need 1 argument: the number n for which to find the first prime number bigger or equal.")
    n = int(sys.argv[1])
    print(first_prime_bigger_than(n))
