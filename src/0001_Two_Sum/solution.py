from typing import List, Dict


class Solution:
    """
    Runtime: 98.09%
    Memory: 19.72%
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            target_num = target - num
            if target_num in nums_map:
                return [idx, nums_map[target_num]]
            nums_map[num] = idx

        raise RuntimeError("Could not find a solution.")
