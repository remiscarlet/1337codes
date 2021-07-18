import collections


class Solution:
    """
    Runtime: 95.82%
    Memory: 80.13%

    Lol.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
