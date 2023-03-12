import pytest

from python.missing_number.missing_number import Solution

@pytest.mark.parametrize('nums, expected_missing',[
    ([3,0,1], 2),
    ([0,1], 2),
    ([9,6,4,2,3,5,7,0,1], 8)
])
def test_given_sentence_when_solution_length_of_last_word_runs_then_returns_expected_length(nums, expected_missing):
    assert Solution().missingNumber(nums) == expected_missing
