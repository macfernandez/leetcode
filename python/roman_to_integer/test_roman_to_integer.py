import pytest

from python.roman_to_integer.roman_to_integer import Solution

@pytest.mark.parametrize('roman, expected_int',[
    ('I', 1),
    ('III', 3),
    ('V', 5),
    ('LVIII', 58),
    ('MCMXCIV', 1994),
    ('DCCCLXXXVIII', 888),
    ('MMMCMXCIX', 3999)
])
def test_given_number_in_roman_when_solution_roman_to_int_runs_then_returns_expected_int(roman, expected_int):
    assert Solution().roman_to_int(roman) == expected_int
