from typing import List


class Solution:
    """
    Runtime: 92.49%
    Memory: 98.47%
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [1] * nums_len
        for idx in range(1, nums_len):
            ans[idx] = ans[idx - 1] * nums[idx - 1]
        r = 1
        for idx in reversed(range(nums_len)):
            ans[idx] *= r
            r *= nums[idx]

        return ans

    def productExceptSelfNaive(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left_sum = [-1] * nums_len
        right_sum = [-1] * nums_len
        left_sum[0] = 1
        right_sum[nums_len - 1] = 1

        for idx in range(1, nums_len):
            left_sum[idx] = left_sum[idx - 1] * nums[idx - 1]

            r_idx = nums_len - 1 - idx
            right_sum[r_idx] = right_sum[r_idx + 1] * nums[r_idx + 1]

        # print(left_sum)
        # print(right_sum)

        return [left_sum[idx] * right_sum[idx] for idx in range(nums_len)]
