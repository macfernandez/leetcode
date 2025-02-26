
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
def test_solution(
    list_node_for_testing, l1, l2, expected_list_node
    ):
    l1, l2 = list_node_for_testing(l1), list_node_for_testing(l2)
    expected = list_node_for_testing(expected_list_node)
    predicted = Solution().addTwoNumbers(l1, l2)
    while True:
        assert expected.val == predicted.val
        if expected.next is None and predicted.next is None:
            break
        expected, predicted = expected.next, predicted.next
        