"""Unit tests for ...

(c) Raise Partner 2022
Vincent Pfister
"""
import pytest

from pb2278.percentage import Solution


@pytest.mark.parametrize(("s", "letter", "expected"), [
    pytest.param("foobar", "o", 33, id="ex1"),
    pytest.param("jjjj", "k", 0, id="ex2"),
    pytest.param("", "k", 0, id="empty"),
])
def test_percentage_letter(s: str, letter: str, expected: int):
    assert Solution().percentageLetter(s, letter) == expected
