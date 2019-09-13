"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    """
      Check if number (given in function parameter) is prime.

      If number is prime -> return True
      If number is not prime -> return False

      :param number: number for check.
      :return: boolean True if number is prime or False if number is not prime.
      """
    if number > 1:
        if number == 2:
            return True
        for i in range(2, number):
            if (number % i) == 0:
                return False
            else:
                return True
    else:
        return False


if __name__ == '__main__':
    print(is_prime_number(2))
    print(is_prime_number(89))
    print(is_prime_number(23))
    print(is_prime_number(4))
    print(is_prime_number(7))
    print(is_prime_number(88))
