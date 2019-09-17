"""Converter."""


def dec_to_binary(dec: int) -> str:
    """
    Convert decimal number into binary.

    :param dec: decimal number to convert
    :return: number in binary
    """
    result = ""
    while dec > 1:
        """
        example:    145 % 2 = 1
                    145 // 2 = 72
        """
        result = str(dec % 2) + result
        dec = dec // 2
    return str(dec) + result


def binary_to_dec(binary: str) -> int:
    """
    Convert binary number into decimal.

    :param binary: binary number to convert
    :return: number in decimal
    """
    decimal, exponent = 0, 0
    while binary != 0:
        """
        example:    1111 % 10 = 1
                    1 * 2^0
                    1111 // 10 = 111 etc
                    1*2^0 + 1*2^1 + 1*2^2 + 1*2^3
        """
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
