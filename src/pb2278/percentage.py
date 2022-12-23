class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count_all = len(s)
        if count_all > 0:
            count_letter = sum([1 for c in s if letter == c])
            return (100 * count_letter) // count_all
        return 0

