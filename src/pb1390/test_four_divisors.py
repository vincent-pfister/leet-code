import pytest

from pb1390 import four_divisors
from pb1390.data import DATA_1, DATA_2, DATA_3, MAX_DECREASING


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([12, 60], 0, id="trivial"),
        pytest.param([21, 4, 7], 32, id="example 1"),
        pytest.param([21, 21], 64, id="example 2"),
        pytest.param([1, 2, 3, 4, 5], 0, id="example 3"),
        pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 45, id="count 10"),
        pytest.param([7286, 18704, 70773, 8224, 91675], 10932, id="5 large values"),
        pytest.param(
            DATA_1,
            69399654,
            id="long large 1",
        ),
        pytest.param(
            DATA_2,
            135341358,
            id="long large 2",
        ),
        pytest.param(
            DATA_3,
            134716980,
            id="long large 3",
        ),
        pytest.param([105] * 104, 0, id="max count"),
        pytest.param(
            MAX_DECREASING,
            2371,
            id="max decreasing",
        ),
    ],
)
def test_four_divisor(nums: list[int], expected: int) -> None:
    assert four_divisors.Solution().sumFourDivisors(nums) == expected
