import pytest

from top_interview_150.best_time_to_buy_and_sell_stock.best_time_to_buy_and_sell_stock import Solution


@pytest.mark.parametrize("prices, expected_output", [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0)
])
def test_solution(prices, expected_output):
    assert Solution().maxProfit(prices) == expected_output