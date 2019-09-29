"""Filtering."""


def remove_vowels(string: str) -> str:
    """
    Remove vowels (a, e, i, o, u).

    :param string: Input string
    :return string without vowels.
    """
    newstr = string
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for x in string:
        if x in vowels:
            newstr = newstr.replace(x, "")
    return newstr


def longest_filtered_word(string_list: list) -> str:
    """
    Filter, find and return the longest string.

    :param string_list: List of strings.
    :return: Longest string without vowels.
    """
    for string in string_list:
        string = remove_vowels(string)
    longest_string = max(string_list, key=len)
    return longest_string


def sort_list(string_list: list) -> list:
    """
    Filter vowels in strings and sort the list by the length.

    Longer strings come first.

    :param string_list: List of strings that need to be sorted.
    :return: Filtered list of strings sorted by the number of symbols in descending order.
    """
    for x in string_list:
        string_list = remove_vowels(x)
        return string_list


if __name__ == '__main__':
    print(remove_vowels(""))  # => ""
    print(remove_vowels("hello"))  # => "hll"
    print(remove_vowels("Home"))  # => "Hm"
    print(longest_filtered_word(["Bunny", "Tiger", "Bear", "Snake"]))  # => "Bnny"
    print(sort_list(["Bunny", "Tiger", "Bear", "Snake"]))  # => ['Bnny', 'Tgr', 'Snk', 'Br']
