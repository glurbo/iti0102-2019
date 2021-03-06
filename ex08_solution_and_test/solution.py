"""Solution."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time in range(18, 25) and not coffee_needed:
        return True
    elif time in range(5, 18) and coffee_needed:
        return True
    elif time in range(1, 5):
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c:
        if a == 5:
            return 10
        elif a in range(0, 5):
            return 5
    elif a != b:
        if a != c:
            return 1
        elif a == c:
            return 0
    elif a == b:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    big_baskets_kg = big_baskets * 5
    if big_baskets_kg + small_baskets >= ordered_amount:
        result = ordered_amount - big_baskets_kg
        return result
    else:
        return -1
