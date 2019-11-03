import pytest
import filter
import random


def test_remove_vowels_when_no_vowels():
    random_string_list = random.choices("asdf", k=10)
    random_string_list += random.choices("asdf", k=12)
    random.shuffle(random_string_list)


def test_remove_vowels():
    assert filter.remove_vowels("a") == ""
    assert filter.remove_vowels("b") == "b"


def test_remove_vowels_uppercase():
    for v in "AEIOU":
        assert filter.remove_vowels(v) == "", "Upper vowel should be removed."


#def test_remove_vowels_only_vowels_return_empty():


#def test_remove_vowels_empty_string():


#def test_remove_vowels_mixed_letters():


#def test_longest_filtered_word():


#def test_longest_filtered_word_first_in_order():


#def test_longest_filtered_word_one_empty_string():


#def test_longest_filtered_word_empty_list():


#def test_longest_filtered_word_filter_before_taking_longest():


#def test_longest_filtered_word_important_order():


#def test_sort_list_only_one_way():


#def test_sort_list_two_order_options():


#def test_sort_list_multiple_order_options():


#def test_sort_list_empty_list():


#def test_random_longest_and_sort():