"""Recursion is recursion."""


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    recursive_reverse("") => ""
    recursive_reverse("abc") => "cba"

    :param s: string
    :return: reverse of s
    """
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def remove_nums_and_reverse(string):
    """
    Recursively remove all the numbers in the string and return reversed version of that string without numbers.

    print(remove_nums_and_reverse("poo"))  # "oop"
    print(remove_nums_and_reverse("3129047284"))  # empty string
    print(remove_nums_and_reverse("34e34f7i8l 00r532o23f 4n5oh565ty7p4"))  # "python for life"
    print(remove_nums_and_reverse("  k 4"))  # " k  "

    :param string: given string to change
    :return: reverse version of the original string, only missing numbers
    """


def task1(string):
    """
    Figure out what this code is supposed to do and rewrite it using recursion.

    :param string: given string
    :return: figure it out
    """
    # palindrome function
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return task1(string[1:-1])


def task2(string):
    """
    Figure out what this code is supposed to do and rewrite it using iteration.

    :param string: given string
    :return: figure it out
    """
    # adds dash("-") in between repeating characters
    if len(string) < 2:
        return string
    for i in range(len(string)):
        if string[i] == string[i-1]:
            "-".join([string[i-1], string[i]])
    return string


if __name__ == '__main__':
    print(recursive_reverse("abc"))
    print(recursive_reverse(""))

    print(task1("racecar"))
    print(task2("12334566"))
