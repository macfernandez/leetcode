import pytest

from python.plus_one.plus_one import Solution

@pytest.mark.parametrize('sentence, expected_length',[
    ([1,2,3], [1,2,4]),
    ([4,3,2,1], [4,3,2,2]),
    ([9], [1,0]),
    ([1,9,3], [1,9,4])
])
def test_given_sentence_when_solution_length_of_last_word_runs_then_returns_expected_length(sentence, expected_length):
    assert Solution().plus_one(sentence) == expected_length
