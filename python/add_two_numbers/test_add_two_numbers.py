
import pytest

from python.add_two_numbers.add_two_numbers import Solution, ListNode


@pytest.fixture
def list_node_for_testing():
    def list_node(nodes):
        for i, n in enumerate(nodes[::-1]):
            if i == 0:
                node = ListNode(n)
            else:
                node = ListNode(n, next=node)
        return node
    return list_node

@pytest.mark.parametrize('l1, l2, expected_list_node',[
    ([2,4,3], [5,6,4], [7,0,8]),
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1])
])
def test_given_two_list_node_when_add_two_numbers_runs_then_returns_expected_list_node(
    list_node_for_testing, l1, l2, expected_list_node
    ):
    assert True
