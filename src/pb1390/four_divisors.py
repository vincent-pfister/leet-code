import math


def get_divisors_sum(num: int) -> int:
    v = num
    i = 2
    divs = set()
    upper = int(math.floor(math.sqrt(v)))
    while i <= upper and len(divs) <= 2:
        if v % i == 0:
            v = v // i
            divs.update((i, v))
            if len(divs) > 2:
                return 0
            upper = int(math.floor(math.sqrt(v)))
        else:
            i += 1
    if len(divs) == 2:
        return 1 + num + sum(divs)
    return 0


class Solution:

    def sumFourDivisors(self, nums: list[int]) -> int:
        return sum(get_divisors_sum(num) for num in nums)
