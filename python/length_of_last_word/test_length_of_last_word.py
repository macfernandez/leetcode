import pytest

from python.length_of_last_word.length_of_last_word import Solution

@pytest.mark.parametrize('s, expected_length', [
    ('Hello World', 5),
    ('   fly me   to   the moon  ', 4),
    ('luffy is still joyboy', 6)
])
def test_given_string_when_length_of_last_word_runs_then_returns_expected_word_length(s, expected_length):
    assert Solution().length_of_last_word(s) == expected_length