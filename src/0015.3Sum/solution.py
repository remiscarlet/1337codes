from typing import List


class Solution:
    """
    Runtime: 94.70%
    Memory: 73.39%
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3:
            return []

        nums = sorted(nums)

        def twoSum(left_edge_idx: int, target_sum: int) -> List[List[int]]:
            l = left_edge_idx + 1
            r = nums_len - 1
            sums = []

            while l < r:
                l_num, r_num = nums[l], nums[r]
                curr_sum = l_num + r_num
                if curr_sum > target_sum:
                    r -= 1
                elif curr_sum < target_sum:
                    l += 1
                else:
                    sums.append([l_num, r_num])
                    r -= 1
                    l += 1
                    while l < nums_len and nums[l] == l_num:
                        l += 1
            return sums

        results = []
        prev_val = None
        for idx, val in enumerate(nums):
            if val == prev_val:
                continue
            elif val > 0:
                break  # If sorted, nothing to the right (positive) can sum to a negative

            target_sum = -1 * val
            sums = twoSum(idx, target_sum)

            for arr in sums:
                results.append([val] + arr)

            prev_val = val

        return results

    def threeSumNaive(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3:
            return []
        if list(filter(lambda val: val != 0, nums)) == []:
            return [[0, 0, 0]]

        twosum_memo = {}

        def twosum(target_sum: int, arr: List[int]) -> List[List[int]]:
            sums = []
            cache = set()
            for idx, first_val in enumerate(arr):
                target_second_val = target_sum - first_val
                if target_second_val in cache:
                    sums.append([first_val, target_second_val])
                cache.add(first_val)

            twosum_memo[target_sum] = sums
            return sums

        valid_sums = []
        for idx, num in enumerate(nums):
            target_sum = -1 * num
            if target_sum in twosum_memo:
                continue

            sum_arrs = twosum(target_sum, nums[:idx] + nums[idx + 1 :])

            if sum_arrs != []:
                for sum_arr in sum_arrs:
                    valid_sums.append([nums[idx]] + sum_arr)

        sums = set()
        for arr in valid_sums:
            tup = tuple(sorted(arr))
            sums.add(tup)

        return list(map(list, sums))
