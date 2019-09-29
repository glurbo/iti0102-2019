# -*- coding: utf-8 -*-
"""Check if given ID code is valid."""


def is_valid_gender_number(gender_number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number in range(1, 7):
        return True
    else:
        return False


def is_leap_year(year_number: int) -> bool:
    """
    Check if given value is a leap year or not.

    :param year_number: int
    :return: boolean
    """
    if year_number % 4 == 0:
        if year_number % 100 == 0:
            if year_number % 400 == 0:
                return True
            else:
                return False
        return True
    else:
        return False


def get_gender(gender_number: int) -> str:
    """
    Check if given value is male or female.

    :param gender_number: int
    :return: str
    """
    male = [1, 3, 5]
    female = [2, 4, 6]
    if gender_number in male:
        return "male"
    elif gender_number in female:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number in range(100):
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if month_number in range(13):
        return True
    else:
        return False


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    monthlist1 = [1, 3, 5, 7, 8, 10, 12]
    monthlist2 = [4, 6, 9, 11]
    monthlist3 = [2]
    if month_number in monthlist1:
        if day_number in range(1, 32):
            return True
        else:
            return False
    elif month_number in monthlist2:
        if day_number in range(1, 31):
            return True
        else:
            return False
    elif month_number in monthlist3:
        if is_leap_year(get_full_year(gender_number, year_number)):
            if day_number in range(1, 30):
                return True
            else:
                return False
        else:
            if day_number in range(1, 28):
                return True
            else:
                return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if birth_number in range(1, 1000):
        return True
    else:
        return False


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    sum = 1 * int(id_code[:1]) + 2 * int(id_code[1:2]) + 3 * int(id_code[2:3]) + 4 * int(id_code[3:4]) + 5 * \
        int(id_code[4:5]) + 6 * int(id_code[5:6]) + 7 * int(id_code[6:7]) + 8 * int(id_code[7:8]) + 9 *\
        int(id_code[8:9]) + 1 * int(id_code[9:10])
    control_number = sum % 11
    if int(control_number) == int(id_code[10:11]):
        return True
    elif int(control_number) == 10:
        sum = 3 * int(id_code[:1]) + 4 * int(id_code[1:2]) + 5 * int(id_code[2:3]) + 6 * int(id_code[3:4]) + 7 * \
            int(id_code[4:5]) + 8 * int(id_code[5:6]) + 9 * int(id_code[6:7]) + 1 * int(id_code[7:8]) + 2 * \
            int(id_code[8:9]) + 3 * int(id_code[9:10])
        control_number = sum % 11
        if control_number == int(id_code[10:11]):
            return True
        elif control_number == 10:
            if int(id_code[10:11]) == 0:
                return True
            else:
                return False
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    if gender_number in range(1, 3):
        full_year = "18" + "{:02d}".format(year_number)
        return int(full_year)
    elif gender_number in range(3, 5):
        full_year = "19" + "{:02d}".format(year_number)
        return int(full_year)
    elif gender_number in range(5, 7):
        full_year = "20" + "{:02d}".format(year_number)
        return int(full_year)


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    Paide, Rakvere, Valga, Viljandi, Võru and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'

    :param birth_number: int
    :return: str
    """
    d = {tuple(range(1, 11)): 'Kuressaare',
         tuple((range(11, 21), range(271, 371))): 'Tartu',
         tuple((range(21, 221), range(471, 491))): 'Tallinn',
         tuple(range(371, 421)): 'Kohtla-Järve',
         range(371, 421): 'Narva',
         range(421, 471): 'Pärnu',
         range(491, 521): 'Paide',
         range(521, 571): 'Rakvere',
         range(571, 601): 'Valga',
         range(601, 651): 'Viljandi',
         range(651, 711): 'Võru',
         range(711, 1000): 'unidentified'}
    if is_valid_birth_number(birth_number):
        for key, value in d.items():
            if key == birth_number:
                return d[value]
    else:
        return "Wrong input!"


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    if is_valid_control_number(id_code):
        return f"This is a {get_gender(int(id_code[0:1]))} born on {id_code[5:7]}.{id_code[3:5]}." \
               f"{get_full_year(int(id_code[0:1]), int(id_code[1:3]))} in {get_birth_place(int(id_code[7:10]))}"
    else:
        return "Given invalid ID code!"


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    if is_valid_gender_number(int(id_code[0:1])):
        if is_valid_year_number(int(id_code[1:3])):
            if is_valid_month_number(int(id_code[3:5])):
                if is_valid_day_number(int(id_code[0:1]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])):
                    if is_valid_birth_number(int(float(id_code[7:10]))):
                        if is_valid_control_number(id_code):
                            return True
                    else:
                        return False
                else:
                    return False

            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False
    print("\nDay number:")
    print(is_valid_day_number(4, 5, 12, 25))  # -> True
    print(is_valid_day_number(3, 10, 8, 32))  # -> False
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(
        is_valid_day_number(4, 96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(is_valid_day_number(4, 99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(is_valid_day_number(4, 8, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(is_valid_day_number(4, 22, 4, 31))  # -> False (April contains max 30 days)
    print(is_valid_day_number(4, 18, 10, 31))  # -> True
    print(is_valid_day_number(4, 15, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
    print("\nControl number:")
    print(is_valid_control_number("49808270244"))  # -> True
    print(is_valid_control_number("60109200187"))  # -> False, it must be 6

    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998 in Tallinn."
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    # Comment these back in if you have completed other functions.
    print("\nChecking where the person was born")

    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"

    print("\nOverall ID check::")
    print(is_id_valid("49808270244"))  # -> True
    print(is_id_valid("12345678901"))  # -> False
    print("\nTest now your own ID code:")
    personal_id = input()  # type your own id in command prompt
    print(is_id_valid(personal_id))  # -> True
