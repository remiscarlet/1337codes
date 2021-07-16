import functools
from typing import List


class Solution:
    """
    Runtime: 84.62%
    Memory: 86.64%
    """

    def maxArea(self, heights: List[int]) -> int:
        l = max_fill = 0
        r = len(heights) - 1

        while l < r:
            l_h = heights[l]
            r_h = heights[r]
            fill = min(l_h, r_h) * (r - l)

            if max_fill < fill:
                max_fill = fill

            if l_h < r_h:
                l += 1
            else:
                r -= 1

        return max_fill

    def maxAreaNaive(self, heights: List[int]) -> int:
        height_order = list(enumerate(heights))
        sorted_height_order = sorted(height_order, key=lambda tup: tup[1], reverse=True)

        max_fill = -1
        for sort_idx, height_data in enumerate(sorted_height_order):
            height_idx, height = height_data
            taller_heights = sorted_height_order[:sort_idx]
            if len(taller_heights) == 0:
                continue

            farthest_line = functools.reduce(
                lambda x, y: x
                if abs(height_idx - x[0]) > abs(height_idx - y[0])
                else y,
                taller_heights,
            )

            taller_height_idx, taller_height = farthest_line

            fill = height * abs(height_idx - taller_height_idx)

            if fill > max_fill:
                max_fill = fill

        return max_fill
