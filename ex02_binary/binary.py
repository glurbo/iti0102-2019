"""Converter."""


def dec_to_binary(decimal: int) -> str:
    """
    Convert decimal number into binary.

    :param decimal: decimal number to convert
    :return: number in binary
    """
    if decimal == 0:
        return str(decimal)
    elif decimal >= 1:
        binary = decimal // 2
        print(binary % 2, end='')
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


import csv
# import csv is REQUIRED to read in csv file



with open('C:\\Projects\\kool\\decimal_binary_numbers\\numbers.csv', 'r') as f:
    reader = csv.reader(f)
    decimal_binary_list = list(reader)

    print("DECIMAL TO BINARY")
    for numbers in decimal_binary_list:
        # decimal x in binary is y: True/False
        print(f"decimal {numbers.__getitem__(0)} in binary is {numbers.__getitem__(1)}: "
              f"{dec_to_binary(int(numbers.__getitem__(0))) == numbers.__getitem__(1)}")

    print("BINARY TO DECIMAL")
    for numbers in decimal_binary_list:
        # binary x in decimal is x: True/False
        print(f"binary {numbers.__getitem__(1)} in decimal is {numbers.__getitem__(0)}: "
              f"{binary_to_dec(numbers.__getitem__(1)) == int(numbers.__getitem__(0))}")