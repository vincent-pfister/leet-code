from typing import Iterable

import numpy as np
import pytest

from pb1687.boxes import Solution
from pb1687.cases import BOXES_1, BOXES_2, BOXES_3, BOXES_4


@pytest.mark.parametrize(
    ("boxes", "ports_count", "max_boxes", "max_weight", "expected"),
    [
        pytest.param([[1, 1], [2, 1], [1, 1]], 2, 3, 3, 4, id="ex1"),
        pytest.param([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 3, 6, 6, id="ex2"),
        pytest.param(
            [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7, 6, id="ex3"
        ),
        pytest.param(
            [[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 6, 6, id="ex4"
        ),
        pytest.param(
            [[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]],
            5,
            5,
            7,
            14,
            id="case1",
        ),
        pytest.param(
            [[1, 1], [2, 1], [1, 1], [2, 1], [1, 1], [2, 1]],
            2,
            10,
            10,
            7,
            id="case2",
        ),
        pytest.param(BOXES_1, 100000, 60000, 100000, 18455, id="long1"),
        pytest.param(BOXES_2, 216, 3, 47520, 857, id="long2"),
        pytest.param(BOXES_3, 10, 10000, 10000, 90062, id="long3"),
        pytest.param(BOXES_4, 77, 17, 93070, 214, id="weight max 1"),
    ],
)
def test_box_delivering(
    boxes: list[list[int]],
    ports_count: int,
    max_boxes: int,
    max_weight: int,
    expected: int,
):
    assert (
        Solution().boxDelivering(boxes, ports_count, max_boxes, max_weight) == expected
    )


A = np.array([1, 3, 5, 2, 1, 2])
AC = np.array([1, 4, 9, 11, 12, 14])


@pytest.mark.parametrize(
    ("max_count", "max_sum", "expected"),
    [
        pytest.param(6, 12, 5, id="before last"),
        pytest.param(6, 14, 6, id="last"),
        pytest.param(6, 15, 6, id="after last"),
        pytest.param(6, 2, 1, id="after first"),
        pytest.param(4, 7, 2, id="before last, shorter"),
    ],
)
def test_searchsorted(max_count: int, max_sum: int, expected: int) -> None:
    actual = np.searchsorted(AC[:max_count], max_sum, side="right")
    assert actual == expected
