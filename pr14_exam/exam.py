"""PR14 Exam."""


def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.
    If duplicate keys in the new dictionary exist, leave the first one.
    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}

    :param dic: original dictionary
    :return: dictionary where keys and values are swapped
    """
    new_d = {}
    #  return dict((v, k) for k, v in dic.items())
    for k, v in dic.items():
        if v in new_d:
            continue
        new_d[v] = k
    return new_d


def find_divisors(number) -> list:
    """
    The task is to find all the divisors for given number in range to the given number's value.
    Divisor - a number that divides evenly into another number.
    Return list of given number divisors in ascending order.
    NB! Numbers 1 and number itself must be excluded if there are more divisors
    than 1 and number itself!
    (138) > [2, 3, 6, 23, 46, 69]
    (3) > [1, 3]
    :param number: int
    :return: list of number divisors
    """
    lis = []
    for i in range(2, number):
        if number % i == 0:
            lis.append(i)
    if len(lis) == 0:
        for i in range(1, number + 1):
            if number % i == 0:
                lis.append(i)
    return lis


def sum_of_multiplies(first_num, second_num, limit) -> int:
    """
    The task is to find all the multiplies of each given of two numbers within the limit.
    Then, find the sum of those multiplies.
    (3, 5, 20) => 98 (3 + 6 + 9 + 12 + 15 + 18 + 5 + 10 + 20) 15 is included only once
    (3, 3, 10) => 18 (3 + 6 + 9)
    (3, 10, 2) => 0
    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    count1 = 1
    count2 = 1
    result = []
    for i in range(limit + 1):
        if (count1 * first_num) > limit:
            break
        result.append(count1 * first_num)
        count1 += 1
    for i in range(limit + 1):
        if (count2 * second_num) > limit:
            break
        if (count2 * second_num) in result:
            result.remove(count2 * second_num)
        result.append(count2 * second_num)
        count2 += 1
    return sum(result)


def count_odds_and_evens(numbers: list) -> str:
    """
    The task is to count how many odd and even numbers does the given list contain.
    Do not count zeros (0).
    Result should be displayed as string "ODDS: {number of odds}\nEVENS: {number of evens}"

    count_odds_and_events([1, 2, 3]) => "ODDS: 2\nEVENS: 1"
    count_odds_and_events([1, 0]) => "ODDS: 1\nEVENS: 0"

    :param numbers: list
    :return: str
    """
    number_of_odds = 0
    number_of_evens = 0
    for i in numbers:
        if i == 0:
            continue
        elif i % 2 == 0:
            number_of_evens += 1
        else:
            number_of_odds += 1
    return f"ODDS: {number_of_odds}\nEVENS: {number_of_evens}"


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5
    """
    lis = []
    count = False
    for i in numbers:
        if i == 5:
            count = False
        if count is True:
            lis.append(i)
        if i == 2:
            count = True
    return sum(lis)


def transcribe(dna_strand: str):
    """
    Write a function that returns a transcribed RNA strand from the given DNA strand,
    that is formed by replacing each nucleotide(character) with its complement: G => C, C => G, T => A, A => U
    Return None if it is not possible to transcribe a DNA strand.
    Empty string should return empty string.

    "ACGTGGTCTTAA" => "UGCACCAGAAUU"
    "gcu" => None

    :param dna_strand: original DNA strand
    :return: transcribed RNA strand in the uppercase or None
    """
    if dna_strand == "":
        return ""
    dna_strand = list(dna_strand)
    for i in range(0, len(dna_strand)):
        if dna_strand[i] == "G":
            dna_strand[i] = "C"
        elif dna_strand[i] == "C":
            dna_strand[i] = "G"
        elif dna_strand[i] == "T":
            dna_strand[i] = "A"
        elif dna_strand[i] == "A":
            dna_strand[i] = "U"
        else:
            return None
    return "".join(dna_strand)


def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    new_d = {}
    #  new_d = {k: v for k, v in d1.items() if k in d2}
    for k, v in d1.items():
        if (k, v) in d2.items():
            new_d[k] = v
    return new_d


def reserve_list(input_strings: list) -> list:
    """
    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    ['apple', 'banana', 'onion'] -> ['noino', 'ananab', 'elppa']
    ['lollipop', 'python', 'candy'] -> ['candy', 'python', 'popillol']
    ['sky', 'python', 'candy', 'java', 'fly'] -> ['ylf', 'java', 'candy', 'python', 'yks']
    ['sky', 'python', 'java', 'candy'] -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    no_reverse = True
    for i in range(0, len(input_strings)):
        if input_strings[i] == "python":
            no_reverse = False
        elif input_strings[i] == "java":
            no_reverse = True
        elif no_reverse:
            input_strings[i] = input_strings[i][::-1]

    return input_strings[::-1]


def convert_binary_to_decimal(binary_list: list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.

    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    num = "".join(str(v) for v in binary_list)
    dec_value = 0
    base = 1

    temp = num
    while temp:
        last_digit = int(temp) % 10
        temp = int(temp) / 10

        dec_value += last_digit * base
        base = base * 2
    return dec_value


def print_pages(pages: str) -> list:
    """
    Find pages to print in console.

    examples:
    print_pages("2,4,9") -> [2, 4, 9]
    print_pages("2,4-7") -> [2, 4, 5, 6, 7]
    print_pages("2-5,7,10-12,17") -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
    print_pages("1,1") -> [1]
    print_pages("") -> []
    print_pages("2,1") -> [1, 2]

    :param pages: string containing page numbers and page ranges to print.
    :return: list of pages to print with no duplicates, sorted in increasing order.
    """
    if len(pages) == 0:
        return list(pages)
    pages = pages.split(",")
    return pages


if __name__ == '__main__':
    print(swap_items({"a": 1, "b": 2, "c": 3}))
    print(swap_items({"Morning": "Good", "Evening": "Good"}))
    print("-------------------------------")
    print(find_divisors(138))
    print(find_divisors(3))
    print("-------------------------------")
    print(sum_of_multiplies(3, 5, 20))
    print(sum_of_multiplies(3, 3, 10))
    print(sum_of_multiplies(3, 10, 2))
    print("-------------------------------")
    print(count_odds_and_evens([1, 2, 3]))
    print(count_odds_and_evens([1, 0]))
    print("-------------------------------")
    print(sum_between_25([1, 3, 6, 7]))  # = > 0
    print(sum_between_25([1, 2, 3, 4, 5, 6]))  # = > 7
    print(sum_between_25([1, 2, 3, 4, 6, 6]))  # = > 19
    print(sum_between_25([1, 3, 3, 4, 5, 6]))  # = > 0
    print(sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]))  # = > 16
    print(sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]))  # = > 5
    print("-------------------------------")
    print(transcribe("ACGTGGTCTTAA"))  # = > "UGCACCAGAAUU"
    print(transcribe("gcu"))  # = > None
    print("-------------------------------")
    print(union_of_dict({"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 42}))  # == > {"a": 1}
    print(union_of_dict({}, {"bar": "foo"}))  # = > {}
    print("-------------------------------")
    print(reserve_list(['apple', 'banana', 'onion']))  # -> ['noino', 'ananab', 'elppa']
    print(reserve_list(['lollipop', 'python', 'candy']))  # -> ['candy', 'python', 'popillol']
    print(reserve_list(['sky', 'python', 'candy', 'java', 'fly']))  # -> ['ylf', 'java', 'candy', 'python', 'yks']
    print(reserve_list(['sky', 'python', 'java', 'candy']))  # -> ['ydnac', 'java', 'python', 'yks']
    print("-------------------------------")
    print(convert_binary_to_decimal([0, 0, 0, 0]))
    print(convert_binary_to_decimal([0, 1, 0, 0]))
    print("-------------------------------")
    print(print_pages("2,4,9"))  # -> [2, 4, 9]
    print(print_pages("2,4-7"))  # -> [2, 4, 5, 6, 7]
    print(print_pages("2-5,7,10-12,17"))  # -> [2, 3, 4, 5, 7, 10, 11, 12, 17]
    print(print_pages("1,1"))  # -> [1]
    print(print_pages(""))  # -> []
    print(print_pages("2,1"))  # -> [1, 2]
