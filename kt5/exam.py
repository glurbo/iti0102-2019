"""KT5 (R10)."""

def get_date_string(date: list) -> str:
    """
    Pretty print the date.

    You are given a list with three numbers where:
    1. First number is day number.
    2. Second number is month number.
    3. Third number is year number.

    Assume that all numbers are always in correct ranges.

    Return the pretty version of the date following the format:
    "The date is -> {day number}/{month number}/{year number}"

    If the list is empty or its length is not 3, return "The date is unknown!"

    print_date([3, 3, 2000]) -> "The date is -> 3/3/2000"
    print_date([20, 12, 5677]) -> "The date is -> 20/12/5677"
    print_date([2, 2, 3, 200]) -> "The date is unknown!"
    print_date([]) -> "The date is unknown!"

    :param date: Input list with day, month and year numbers.
    :return: Pretty version of this date.
    """
    if len(date) == 3:
        return f"The date is -> {date[0]}/{date[1]}/{date[2]}"
    else:
        return "The date is unknown!"


def sum_elements_around_last_three(nums: list) -> int:
    """
    Given a list of ints.

    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_before_and_after_last_three([1, 3, 7]) -> 8
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_before_and_after_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    if 3 not in nums or len(nums) < 2:
        return 0
    if 3 not in nums[:len(nums) - 1] or 3 not in nums[1:]:
        return 0
    nums = nums[::-1]
    for i in range(len(nums) - 1):
        if nums[i] == 3:
            if i == 0:
                continue
            return nums[i - 1] + nums[i + 1]
    #for i in reversed(nums):
    #    if nums[i] == 3:
    #        return nums[i - 1] + nums[i + 1]



def pentabonacci(n: int) -> int:
    """
    Find the total number of odd values in the sequence up to the f(n) [included].

    The sequence is defined like this:
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 4
    f(n) = f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4) + f(n - 5)

    Keep in mind that 1 is the only value that is duplicated in the sequence
    and must be counted only once.

    pentabonacci(5) -> 1
    pentabonacci(10) -> 3
    pentabonacci(15) -> 5

    :param n: The last term to take into account.
    :return: Total number of odd values.
    """
    return (n - 1) + (n - 2) + (n - 3) + (n - 4) + (n - 5)


if __name__ == '__main__':
    print(get_date_string([3, 3, 2000]))  # -> "The date is -> 3/3/2000"
    print(get_date_string([20, 12, 5677]))  # -> "The date is -> 20/12/5677"
    print(get_date_string([2, 2, 3, 200]))  # -> "The date is unknown!"
    print(get_date_string([]))  # -> "The date is unknown!
    print("------------------------------------------------")
    print(sum_elements_around_last_three([1, 3, 7]))  # -> 8
    print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]))  # -> 9
    print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]))  # -> 5
    print(sum_elements_around_last_three([1, 2, 3])) # -> 0
    print("------------------------------------------------")
    print(pentabonacci(5))  # -> 1
    print(pentabonacci(10))  # -> 3
    print(pentabonacci(15))  # -> 5
    nums = [1, 2, 3]
    print(nums[:len(nums) - 1])