import pytest

from top_interview_150.best_time_to_buy_and_sell_stock_ii.best_time_to_buy_and_sell_stock_ii import Solution


@pytest.mark.parametrize("prices, expected_output", [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
    ([2,1,2,0,1], 2),
    ([3,3,5,0,0,3,1,4], 8)
])
def test_solution(prices, expected_output):
    assert Solution().maxProfit(prices) == expected_output