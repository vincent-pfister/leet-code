"""Module.

(c) Raise Partner 2022
Vincent Pfister
"""
import pytest

from pb1728.cat_mouse import Board, Solution

GRID_4 = ["........", "F...#C.M", "........"]

GRID_1 = ["####F", "#C...", "M...."]
GRID_2 = ["M.C...F"]
GRID_3 = ["M.C...F"]
GRID_5 = [
    ".M...",
    "..#..",
    "#..#.",
    "C#.#.",
    "...#F"
]


class TestBoard:

    @pytest.fixture()
    def board(self) -> Board:
        return Board(GRID_1)

    def test_size(self, board):
        assert board.rows == 3
        assert board.cols == 5

    def test_getitem(self, board):
        assert board[1, 1] == 'C'

    def test_cat(self, board):
        assert board.cat == 6

    def test_mouse(self, board):
        assert board.mouse == 10

    def test_food(self, board):
        assert board.food == 4

    def test_mouse_moves(self, board):
        actual = board.get_moves(10, 2)
        assert tuple(sorted(actual)) == (10, 11, 12)

    def test_cat_moves(self, board):
        actual = board.get_moves(6, 1)
        assert tuple(sorted(actual)) == (6, 7, 11)


@pytest.mark.parametrize("grid, cat_jump, mouse_jump, expected", [
    pytest.param(GRID_1, 1, 2, True, id="ex 1"),
    pytest.param(GRID_2, 1, 4, True, id="ex 2"),
    pytest.param(GRID_3, 1, 3, False, id="ex 3"),
    pytest.param(GRID_4, 1, 2, True, id="ex 4"),
    pytest.param(GRID_5, 3, 1, True, id="ex 5"),
])
def test_solution(grid: list[str], cat_jump: int, mouse_jump: int, expected: bool) -> bool:
    actual = Solution().canMouseWin(grid, cat_jump, mouse_jump)
    assert actual == expected
