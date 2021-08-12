from typing import List


class Solution:
    """
    Runtime: 99.78%
    Memory: 78.77%
    """

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) / 2) - sum(nums)
