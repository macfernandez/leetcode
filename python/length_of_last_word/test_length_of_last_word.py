import pytest

from python.length_of_last_word.length_of_last_word import Solution

@pytest.mark.parametrize('sentence, expected_length',[
    ('Hello World', 5),
    ('   fly me   to   the moon  ', 4),
    ('luffy is still joyboy', 6)
])
def test_given_sentence_when_solution_length_of_last_word_runs_then_returns_expected_length(sentence, expected_length):
    assert Solution().lengthOfLastWord(sentence) == expected_length
