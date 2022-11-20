import pytest

from pb2059 import convert


@pytest.mark.parametrize(
    "nums, start, goal, expected",
    [
        pytest.param([2, 4, 12], 2, 12, 2, id="example 1"),
        pytest.param([3, 5, 7], 0, -4, 2, id="example 2"),
        pytest.param([2, 8, 16], 0, 1, -1, id="example 3"),
        pytest.param([1], 0, 3, 3, id="step =1"),
        pytest.param(
            [
                -574938140,
                347713845,
                925500837,
                -396559946,
                -39213216,
                -696511059,
                -701862040,
                -547815957,
                -613314611,
                814380075,
                446824702,
                397447568,
                709912715,
                144793599,
                812441247,
                -59489753,
                857299470,
                360355629,
                85411951,
                -439873837,
                -477453514,
                -887964831,
                -914549223,
                633449658,
                452658511,
                657134722,
                1,
            ],
            827,
            -547815957,
            828,
            id="outside",
        ),
    ],
)
def test_convert(nums: list[int], start: int, goal: int, expected: int):
    assert convert.Solution().minimumOperations(nums, start, goal) == expected
