import pytest

from python.valid_parentheses.valid_parentheses import Solution


@pytest.mark.parametrize('s, expected_validation', [
    ('()', True),
    ('()[]{}', True),
    ('(]', False),
    ('[({}])', False),
    ('[({()})]', True)
])
def test_given_string_with_parentheses_when_valid_parentheses_runs_then_returns_expected_validation(s, expected_validation):
    assert Solution().is_valid(s) == expected_validation