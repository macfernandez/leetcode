import pytest

from python.add_two_numbers.add_two_numbers import Solution

@pytest.mark.parametrize('l1, l2, expected_list_node',[
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])
def test_given_two_list_node_when_add_two_numbers_runs_then_returns_expected_list_node(l1, l2, expected_list_node):
    assert Solution().addTwoNumbers(l1, l2) == expected_list_node

# ERROR: TypeError: object of type 'ListNode' has no len()
