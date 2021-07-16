from typing import List


class Solution:
    """
    Runtime: 92.29%
    Memory: 22.30%
    """

    def search(self, nums: List[int], target: int) -> int:
        def helper(l: int, r: int):
            if l > r:
                return -1

            m = (l + r) // 2
            l_v, m_v, r_v = nums[l], nums[m], nums[r]

            if l_v == target:
                return l
            elif m_v == target:
                return m
            elif r_v == target:
                return r

            if l_v < target and target < m_v:
                return helper(l + 1, m - 1)
            elif m_v < target and target < r_v:
                return helper(m + 1, r - 1)
            if l_v > m_v:
                return helper(l + 1, m - 1)
            else:
                return helper(m + 1, r - 1)

        return helper(0, len(nums) - 1)
