"""Encode and decode text using Rail-fence Cipher."""


def encode(message: str, key: int) -> str:
    """
    Encode text using Rail-fence Cipher.

    Replace all spaces with '_'.

    :param message: Text to be encoded.
    :param key: Encryption key.
    :return: Decoded string.
    """
    result = ""
    message = message.replace(" ", "_")
    increment = 1
    row = 0
    col = 0
    matrix = [["" for _ in range(len(message))] for _ in range(key)]
    for c in message:

        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[row][col] = c

        row += increment
        col += 1

    for i in matrix:
        result += "".join(i)
    return result


def decode(message: str, key: int) -> str:
    """
    Decode text knowing it was encoded using Rail-fence Cipher.

    '_' have to be replaced with spaces.

    :param message: Text to be decoded.
    :param key: Decryption key.
    :return: Decoded string.
    """
    result = ""
    matrix = [["" for _ in range(len(message))] for _ in range(key)]
    idx = 0
    message = message.replace("_", " ")
    increment = 1
    for selectedRow in range(0, len(matrix)):
        row = 0
        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1
            if row == selectedRow:
                matrix[row][col] += message[idx]
                idx += 1
            row += increment
    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)
    return result


def transpose(m):
    """

    :param m:
    :return:
    """
    result = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]
    return result


if __name__ == '__main__':
    print(encode("Mind on vaja krüpteerida", 3))  # => M_v_prido_aaküteiannjred
    print(encode("Mind on", 3))  # => M_idonn
    print(encode("hello", 1))  # => hello
    print(encode("hello", 8))  # => hello
    print(encode("kaks pead", 1))  # => kaks_pead

    print(decode("kaks_pead", 1))  # => kaks pead
    print(decode("M_idonn", 3))  # => Mind on
    print(decode("M_v_prido_aaküteiannjred", 3))  # => Mind on vaja krüpteerida
