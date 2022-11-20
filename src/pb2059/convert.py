from functools import lru_cache


class Solution:
    def __init__(self):
        self.__nums: list[int] = []

    @lru_cache()
    def get_candidates(self, value: int) -> set[int]:
        res = set()
        for num in self.__nums:
            for val in (value + num, value - num, value ^ num):
                res.add(val)
        return res

    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        self.__nums = nums
        current = {goal}
        visited = set()
        steps = 0
        while len(current) > 0:
            steps += 1
            new_values = set()
            for value in current:
                visited.add(value)
                candidates = self.get_candidates(value)
                for c in candidates:
                    if c == start:
                        return steps
                    if c < 0 or c > 1000:
                        continue
                    if c not in visited:
                        new_values.add(c)
            current = new_values
        return -1
