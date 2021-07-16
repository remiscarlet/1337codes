from typing import List


class Solution:
    """
    Runtime: 99.37%
    Memory: 93.33%
    """

    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 1:
            return sum(nums)
        if nums_len <= 3:
            return max(nums)

        max_loots_w_first = [0] * (nums_len + 1)
        max_loots_w_first[1] = nums[0]
        max_loots_wo_first = [0] * (nums_len + 1)

        for idx in range(2, nums_len + 1):
            if idx == nums_len:
                max_loots_w_first[idx] = max_loots_w_first[idx - 1]
            else:
                max_loots_w_first[idx] = max(
                    max_loots_w_first[idx - 1],
                    max_loots_w_first[idx - 2] + nums[idx - 1],
                )

            max_loots_wo_first[idx] = max(
                max_loots_wo_first[idx - 1], max_loots_wo_first[idx - 2] + nums[idx - 1]
            )

        return max(max_loots_w_first[-1], max_loots_wo_first[-1])
