"""Primes identifier."""


def is_prime_number(number: int) -> bool:
    if number > 1:
        for i in range(2, is_prime_number(number)):
            if (number % i) == 0:
                return False
            else:
                return True
    return None


if __name__ == '__is_prime_number__':
    print(is_prime_number(2))
    print(is_prime_number(89))
    print(is_prime_number(23))
    print(is_prime_number(4))
    print(is_prime_number(7))
    print(is_prime_number(88))

"""true true true false true false"""