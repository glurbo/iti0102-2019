"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    if dec > 1:
        dec_to_binary(dec // 2)
        print(dec % 2, end = '')
    return ''


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    decimal, exponent = 0, 0
    while binary != 0:
        dec = int(binary) % 10
        decimal = decimal + dec * pow(2, exponent)
        binary = int(binary) // 10
        exponent += 1
    return decimal


if __name__ == "__main__":
    print(dec_to_binary(145))  # -> 10010001
    print(dec_to_binary(245))  # -> 11110101
    print(dec_to_binary(255))  # -> 11111111

    print(binary_to_dec("1111"))  # -> 15
    print(binary_to_dec("10101"))  # -> 21
    print(binary_to_dec("10010"))  # -> 18
