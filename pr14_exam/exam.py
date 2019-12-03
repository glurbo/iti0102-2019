def swap_items(dic: dict) -> dict:
    """
    Given a dictionary return a new dictionary where keys and values are swapped.
    If duplicate keys in the new dictionary exist, leave the first one.
    {"a": 1, "b": 2, "c": 3} => {1: "a", 2: "b", 3: "c"}
    {"Morning": "Good", "Evening": "Good"} => {"Good": "Morning"}

    :param dic: original dictionary
    :return: dictionary where keys and values are swapped
    """
    pass


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
    pass

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
    pass

def count_odds_and_evens(numbers: list) -> str:
    r"""
    The task is to count how many odd and even numbers does the given list contain.
    Do not count zeros (0).
    Result should be displayed as string "ODDS: {number of odds}\nEVENS: {number of evens}"

    count_odds_and_events([1, 2, 3]) => "ODDS: 2\nEVENS: 1"
    count_odds_and_events([1, 0]) => "ODDS: 1\nEVENS: 0"

    :param numbers: list
    :return: str
    """
    pass

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
    pass


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
    pass

def union_of_dict(d1: dict, d2: dict):
    """
    Given two dictionaries return dictionary that has all the key-value pairs that are the same in given dictionaries.

    union_of_dict({"a": 1, "b": 2, "c":3}, {"a": 1, "b": 42}) ==> {"a": 1}
    union_of_dict({}, {"bar": "foo"}) => {}
    """
    pass

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
     pass

def convert_binary_to_decimal(binary_list: list):
    """
    Extract binary codes of given length from list and convert to decimal numbers.

    [0, 0, 0, 0] => 0.
    [0, 1, 0, 0] => 4.

    :param binary_list: list of 1 and 0 (binary code)
    :return: number converted into decimal system
    """
    pass

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
    pass


"""SIIT ALATES MITTEOLULISED"""


def sum_time(time1: tuple, time2: tuple) -> tuple:
    """
    Add two times represented as tuples.

    #01

    Both arguments represent time in format (hours, minutes).
    A tuple with two integers. The input is always correct (you don't have to check that).
    0 <= hours <= 23
    0 <= minutes <= 59

    sum_time((0, 10), (0, 20)) => (0, 30)
    sum_time((12, 30), (0, 40)) => (13, 10)
    sum_time((23, 20), (2, 40)) => (2, 0)

    :param time1: tuple with two integers: hours, minutes
    :param time2: tuple with two integers: hours, minutes
    :return: sum of time1, time2; tuple with two integers: hours, minutes
    """
    pass


def double_char(original_string: str) -> str:
    """
    Given a string, return a string where for every char in the original is doubled.

    #02

    double_char("a") => "aa"
    double_char("ab") => "aabb"
    double_char("") => ""

    :param str: string
    :return: string where chars are doubled
    """
    pass


def common_elements(list_a: list, list_b: list) -> list:
    """
    Given two lists, return a list of elements that can be found in both input lists.

    #03

    The elements can be in any order. The result should have no duplicates.

    common_elements([1, 2], [2, 1]) => [1, 2]
    common_elements([1, 2], [2, 2, 2]) => [2]
    common_elements([1, 2], []) => []
    common_elements([1, 2, 3], [3, 4, 5, 3]) => [3]
    :param list_a: list
    :param list_b: list
    :return: list of elements found in list_a and list_b
    """
    pass


def reverse_list(input_strings: list) -> list:
    """
    Reverse the list and elements except for "python" and "java" and everything between.

    #04

    Given list of strings, return new reversed list where each list element is
    reversed too. Do not reverse strings followed after element "python". If element is "java" -
    reverse mode is on again.
    P.S - "python" and "java" are not being reversed

    reverse_list(['apple', 'banana', 'onion']) -> ['noino', 'ananab', 'elppa']
    reverse_list(['lollipop', 'python', 'candy']) -> ['candy', 'python', 'popillol']
    reverse_list(['sky', 'python', 'candy', 'java', 'fly']) -> ['ylf', 'java', 'candy', 'python', 'yks']
    reverse_list(['sky', 'python', 'java', 'candy']) -> ['ydnac', 'java', 'python', 'yks']

    :param input_strings: list of strings
    :return: reversed list
    """
    pass


def multiple_elements(items: list) -> dict:
    """
    Given a list of items (strings), return a dict where key is item (string) and value is count.

    #05

    But you are interested only in items which are present more than once.
    So, items with count 1 should not be in the result.

    multiple_items(['a', 'b', 'a']) => {'a': 2}
    multiple_items(['a', 'b', 'c']) => {}
    multiple_items(['a', 'a', 'c', 'c']) => {'a': 2, 'c': 2}

    :param items:
    :return:
    """
    pass


def robot_movement(orders):
    """
    Given a string with robot orders, return the end position and the number of orders executed.

    #06

    The robot knows the following orders:
    - L - turn 90 degrees left
    - R - turn 90 degrees right
    - D - drive 1 step

    There are other orders in the string, but you should ignore those for this exercise.
    In front of an order, there can be a multiplier which indicates how many times the following order is executed.
    For example:
    3D - drives 3 steps
    3L - turns 3 times 90 degree left (when starting heading north, it will then be heading east)
    123D - drives 123 steps
    A - ignore this order
    5A - still ignore (both 5 and A)
    5AD - is the same as just "D"

    The robot starts at (0, 0) heading north. The result should be a tuple in format: (x, y, number of orders executed).
    x grows from west to east, y grows from south to north.

    Examples:

    robot_movement("DDDRDD") => (2, 3, 6)
    robot_movement("RRRLLLL") => (0, 0, 7)
    robot_movement("RRR7L") => (0, 0, 10)
    robot_movement("7A7BD") => (0, 1, 1)

    :param orders:
    :return:
    """
    pass


def sum_digits(num: int) -> int:
    """
    Return sum of digits recursively.

    #09

    Given a positive number as an integer find and return the sum of digits of the number recursively.
    This function CANNOT contain any while/for loops.

    sum_digits(123) => 6
    sum_digits(19) => 10

    :param num: number (int)
    :return: sum of number's digits
    """
    pass


# 07. University imitation


class Book:
    """
    Represent book model.

    When printing the book object, it should show the name.
    """

    def __init__(self, name: str):
        """
        Class constructor. Each book has name.

        :param name: book name
        """
        pass


class Student:
    """
    Represent student model.

    When printing the student object, it should be as: "name(gpa):[book1, book2]"
    ( f"{name}({gpa}):{books}" ).
    """

    def __init__(self, name: str, gpa: float):
        """
        Class constructor.

        Each student has name and gpa (Grade Point Average)
        Student also should have a list of books.

        :param name: student's name
        :param gpa: student's gpa
        """
        pass

    def add_book(self, book: Book):
        """
        Add book to student's bag.

        :param book: Book
        Function does not return anything
        """
        pass

    def can_add_book(self, book: Book):
        """
        Check if given book can be added to student's bag.
        The book can be added if it is not already in student's bag.

        :param book: Book
        :return: bool
        """
        pass

    def get_books(self):
        """
        Return a list of all the books.

        :return: list of Book objects
        """
        pass


class University:
    """
    Represent university model.

    When printing the object, it should be shown as: "name:[student1, student2]"
    ( f"{name}:{students}" ) .
    """

    def __init__(self, name: str, gpa_required: float, books_required: int):
        """
        Class constructor.

        Each university has name, gpa_required and books_required. Last two
        are used to define if student can be added to university.

        University should also have a database to keep track of all students.

        :param name: university name
        :param gpa_required: university required gpa
        :param books_required: university required books amount
        """
        pass

    def enrol_student(self, student: Student):
        """
        Enrol new student to university.

        :param student: Student
        Function does not return anything
        """
        pass

    def can_enrol_student(self, student: Student):
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa
            * he/she has enough amount of books required
            * he/she is not already enrolled to this university

        :return: bool
        """
        pass

    def unenrol_student(self, student: Student):
        """
        Unenrol student from University.

        Student can be unenrolled if he/she actually studies in this university.
        Function does not return anything
        """
        pass

    def get_students(self):
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        pass

    def get_student_highest_gpa(self):
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        pass

    def get_student_max_books(self):
        """
        Return a list of students (student) with the greatest books amount.

        :return: list of Student objects
        """
        pass


# 08. Troll Hunt


class Troll:
    """Troll."""

    def __init__(self, name, weight, height, health_points, stamina_points):
        """
        Constructor.

        :param name: troll name.
        :param weight: troll weight (t).
        :param height: troll height (m).
        :param health_points: troll health points (hp).
        :param stamina_points: troll stamina points (sp).
        """
        pass

    def get_troll_attack_speed(self):
        """
        Get the troll attack speed (1-100), integer.

        The heavier and higher the troll is, the slower it moves.
        The troll speed is calculated using the following formula: 100 / (weight + height).
        Round down.
        Assume that sum of weight and height is always non-negative and smaller or equal to 100.

        EXAMPLE
        --------------------------------------------
        troll weight = 3
        troll height = 20
        then troll speed = 100 / (3 + 20) = 4.347 ~ 4. So the answer is 4.
        --------------------------------------------

        :return: troll attack speed, integer.
        """
        pass

    def get_troll_attack_power(self):
        """
        Get the troll attack power, integer.

        The heavier and higher the troll is, the stronger it is.
        The troll attack power is just the sum of its weight and height.

        EXAMPLE
        --------------------------------------------
        troll weight = 5
        troll height = 20
        then troll attack power = 5 + 20 = 25
        --------------------------------------------

        :return: troll attack power, integer.
        """
        pass

    def get_troll_level(self):
        """
        Get the level of the troll (1-5), integer.

        Each troll has a level, which indicates how dangerous it is in combat.
        The troll level mostly depends on its hp, sp, speed and attack power.
        The level of the troll is calculated using the following formula:

        delta = (5 - 1) / (3000 - 500) = 0.0016
        troll_power = (troll health points + troll stamina points + troll attack speed + troll attack power)

        formula: 0.0016 * (troll_power - 3000) + 5, round down

        EXAMPLE
        --------------------------------------------
        troll hp = 500
        troll stamina = 300
        troll atk speed = 4
        troll atk power = 25

        delta = 0.0016
        troll power = (500 + 300 + 4 + 25) = 829

        troll lvl = 0.0016 * (829 - 3000) + 5) = 1.53 ~= 1
        --------------------------------------------

        :return: troll lvl.
        """
        pass

    def get_name(self):
        """
        Getter.

        :return: troll name.
        """
        pass

    def get_weight(self):
        """
        Getter.

        :return: troll weight.
        """
        pass

    def get_height(self):
        """
        Getter.

        :return: troll height.
        """
        pass

    def get_hp(self):
        """
        Get health points.

        :return: troll hp.
        """
        pass

    def get_sp(self):
        """
        Get stamina.

        :return: troll sp.
        """
        pass

    # add required method(s) to get string representation: f"Name: {troll name}, lvl: {troll lvl}"


class Hunter:
    """Troll hunter."""

    def __init__(self, attack_power, intelligent:bool=False):
        """
        Constructor.

        :param attack_power: Attack power of the hunter.
        :param intelligent: Says for itself.
        """
        pass

    def call_for_help(self):
        """
        If the hunter is intelligent, he can call for help.

        Calling for help increases attack power by 10.
        :return:
        """
        pass

    def get_attack_power(self):
        """
        Getter.

        :return: hunter's atk power.
        """
        pass

    def is_intelligent(self):
        """
        Getter.

        :return: is hunter intelligent? Boolean.
        """
        pass


class Mission:
    """Mission."""

    def __init__(self, hunters, troll):
        """
        Constructor.

        :param hunters: list of hunters obj
        :param troll: troll obj
        """
        pass

    def hunt(self):
        """
        The hunters try to slay down the given troll.

        The hunters succeed if their total attack power is bigger than troll lvl * 300. The troll will become None.
        If their total attack power is smaller than troll lvl * 300, troll kills the most powerful hunter and
        all intelligent hunters call for help.
        If after calling for help total attack power of hunters is still too low, hunters die and the mission is failed.

        If hunters succeed to kill the troll, return true. In other case return false.

        :return: boolean
        """
        pass

    def set_hunters(self, hunters):
        """
        Setter.

        :param hunters: list of hunters obj
        """
        pass

    def set_troll(self, troll):
        """
        Setter.

        Check if troll is Troll class obj and set. In other case do not do anything.

        :param troll: Troll class obj
        """
        pass

    def get_troll(self):
        """
        Getter.

        :return: troll
        """
        pass


if __name__ == '__main__':
    # University examples
    ttu = University('ttu', 60.0, 1)
    print(ttu)  # ttu:[]
    assert str(ttu) == "ttu:[]"

    betty = Student('Betty', 61.0)
    print(betty)  # Betty(61.0):[]
    assert str(betty) == "Betty(61.0):[]"

    print(ttu.can_enrol_student(betty))  # False -> Betty has not enough of books required
    assert not ttu.can_enrol_student(betty)
    print(betty.get_books())  # []
    assert betty.get_books() == []

    math = Book('math')
    print(math)  # math
    assert str(math) == "math"
    betty.add_book(math)
    print(ttu.can_enrol_student(betty))  # True -> now Betty has enough of books required
    assert ttu.can_enrol_student(betty)
    ttu.enrol_student(betty)

    print(ttu)  # ttu:[Betty(61.0):[math]]
    assert str(ttu) == "ttu:[Betty(61.0):[math]]"
    print(betty.can_add_book(math))  # False -> Already has this book
    assert not betty.can_add_book(math)

    economics = Book('economics')
    betty.add_book(economics)
    print(betty.get_books())  # [math, economics]
    assert str(betty.get_books()) == "[math, economics]"

    steven = Student('Steven', 59.0)
    print(ttu.can_enrol_student(steven))  # False -> Not enough high gpa
    assert not ttu.can_enrol_student(steven)

    students = [Student('Sally', 62.0), Student('Ben', 74.6), Student('Ben', 96.1)]

    for student in students:
        student.add_book(math)
        ttu.enrol_student(student)

    print(ttu.students)  # [Betty(61.0):[math, economics], Sally(62.0):[math], Ben(74.6):[math], Ben(96.1):[math]]
    assert str(ttu.students) == "[Betty(61.0):[math, economics], Sally(62.0):[math], Ben(74.6):[math], Ben(96.1):[math]]"
    print(ttu.get_student_highest_gpa())  # [Ben(96.1):[math]]
    assert str(ttu.get_student_highest_gpa()) == "[Ben(96.1):[math]]"
    print(ttu.get_student_max_books())  # [Betty(61.0):[math, economics]]
    assert str(ttu.get_student_max_books()) == "[Betty(61.0):[math, economics]]"

    collin = Student('Collin', 96.1)
    collin.add_book(math)
    collin.add_book(economics)
    ttu.enrol_student(collin)

    print(ttu.get_student_highest_gpa())  # [Ben(96.1):[math], Collin(96.1):[math, economics]]
    assert str(ttu.get_student_highest_gpa()) == "[Ben(96.1):[math], Collin(96.1):[math, economics]]"
    print(ttu.get_student_max_books())  # [Betty(61.0):[math, economics], Collin(96.1):[math, economics]]
    assert str(ttu.get_student_max_books()) == "[Betty(61.0):[math, economics], Collin(96.1):[math, economics]]"

    print("Good job! University done!")  # <- if you reach here, then all example asserts work, good job!

    # Troll hunt
    t1 = Troll("Small Ice troll", 3, 25, 500, 700)
    t2 = Troll("Big Ice troll", 10, 40, 2000, 1500)
    h = Hunter(100, True)
    h1 = Hunter(122)

    hunters1 = [Hunter(50), Hunter(30), Hunter(12)]
    hunters2 = [Hunter(120), Hunter(99), Hunter(98)]
    smart_hunters = [Hunter(0, True) for _ in range(50)]
    hunters2 += smart_hunters

    m = Mission(hunters=hunters1, troll=t1)

    assert t1.get_height() == 25
    assert t1.get_weight() == 3
    assert t1.get_hp() == 500
    assert t1.get_sp() == 700
    assert t1.get_name() == "Small Ice troll"

    assert t1.get_troll_attack_speed() == 3
    assert t1.get_troll_attack_power() == 28
    assert t2.get_troll_attack_power() == 50
    assert t1.get_troll_level() == 2
    assert t2.get_troll_level() == 5

    assert str(t1) == "Name: Small Ice troll, lvl: 2"
    assert str(t2) == "Name: Big Ice troll, lvl: 5"

    assert h.get_attack_power() == 100
    h.call_for_help()
    assert h.get_attack_power() == 110
    h1.call_for_help()
    assert h1.get_attack_power() == 122
    assert h.is_intelligent()

    assert m.get_troll() == t1
    assert not m.hunt()

    m.set_hunters(hunters2)
    assert m.hunt()

    m.set_troll(t2)
    assert not m.hunt()

    print("Good job! Troll hunt works!")