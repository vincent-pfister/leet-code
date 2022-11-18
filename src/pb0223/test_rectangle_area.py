"""Unit tests for ...

(c) Raise Partner 2022
Vincent Pfister
"""
import pytest

from pb0223.rectangle_area import Solution


@pytest.mark.parametrize(
    "ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, expected",
    [
        pytest.param(-3, -3, 0, 0, -2, 1, 4, 3, 21, id="disjoint 1 below 2"),
        pytest.param(-3, 0, 3, 4, 0, -1, 9, 2, 45, id="example 1"),
        pytest.param(-2, -2, 2, 2, -2, -2, 2, 2, 16, id="example 2"),
        pytest.param(-1, -1, 1, 1, -2, -2, 2, 2, 16, id="1st inside"),
        pytest.param(0, 0, 0, 0, -1, -1, 1, 1, 4, id="1st empty inside"),
        pytest.param(-1, -1, 1, 1, 0, 0, 0, 0, 4, id="2nd empty inside"),
    ],
)
def test_area(
    ax1: int,
    ay1: int,
    ax2: int,
    ay2: int,
    bx1: int,
    by1: int,
    bx2: int,
    by2: int,
    expected: int,
) -> None:
    assert Solution().computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) == expected
