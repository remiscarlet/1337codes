from typing import List


class Solution:
    """
    Runtime: 81.02%
    Memory: 47.89%
    """

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        valid_starts = [
            (row, col) for row in range(m) for col in range(n) if grid[row][col] > 0
        ]

        def loot_max_gold(row: int, col: int) -> int:
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0

            gold_here = grid[row][col]
            if gold_here in [0, -1]:
                return 0

            tmp = grid[row][col]
            grid[row][col] = -1

            max_loot_from_next = max(
                loot_max_gold(row + 0, col + 1),
                loot_max_gold(row + 0, col - 1),
                loot_max_gold(row + 1, col + 0),
                loot_max_gold(row - 1, col + 0),
            )

            grid[row][col] = tmp

            gold = gold_here + max_loot_from_next
            return gold

        return max([loot_max_gold(row, col) for row in range(m) for col in range(n)])
