"""Test 2 (R10)."""


def middle_way(a: list, b: list) -> list:
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

    :param a: List of integers of length 3.
    :param b: List of integers of length 3.
    :return: List of integers of length 2.
    """
    new_list = a[1], b[1]
    return list(new_list)


def sorta_sum(a: int, b: int) -> int:
    """
    Given 2 ints, a and b, return their sum.

    However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

    sorta_sum(3, 4) → 7
    sorta_sum(9, 4) → 20
    sorta_sum(10, 11) → 21

    :param a: Integer
    :param b: Integer
    :return: Sum or 20
    """
    result = a + b
    if result in range(10, 20):
        return 20
    else:
        return result


def combo_string(s1: str, s2: str) -> str:
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) > len(s2):
        return s2 + s1 + s2
    elif len(s2) > len(s1):
        return s1 + s2 + s1
    else:
        return ""


def num_as_index(nums: list) -> int:
    """
    Return element which index is the value of the smaller of the first and the last element.

    If there is no such element (index is too high), return the smaller of the first and the last element.

    num_as_index([1, 2, 3]) => 2 (1 is smaller, use it as index)
    num_as_index([4, 5, 6]) => 4 (4 is smaller, but cannot be used as index)
    num_as_index([0, 1, 0]) => 0
    num_as_index([3, 5, 6, 1, 1]) => 5

    :param nums: list of non-negative integers.
    :return: element value in the specific index.
    """
    first = nums[0]
    last = nums[-1]
    if first < last:
        return first


def count_clumps(nums: list) -> int:
    """
    Return the number of clumps in the given list.

    Say that a "clump" in a list is a series of 2 or more adjacent elements of the same value.

    count_clumps([1, 2, 2, 3, 4, 4]) → 2
    count_clumps([1, 1, 2, 1, 1]) → 2
    count_clumps([1, 1, 1, 1, 1]) → 1

    :param nums: List of integers.
    :return: Number of clumps.
    """
    clump = 0
    d = {number: nums.count(number) for number in nums}
    for key, value in d.items():
        if value > 1:
            clump += 1
    return clump


if __name__ == '__main__':
    print(middle_way([1, 2, 3], [4, 5, 6]))
    print(sorta_sum(3, 4))
    print(combo_string('hi', 'Hello'))
    print(num_as_index([1, 2, 3]))
    print(count_clumps([1, 2, 2, 3, 4, 4]))
