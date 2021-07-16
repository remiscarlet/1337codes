class Solution:
    """
    Runtime: 90.00%
    Memory: 62.37%
    """

    def longestPalindrome(self, s: str) -> str:
        slen = len(s)

        def helper(l: int, r: int):
            while l >= 0 and r < slen and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l + 1 : r]

        longest_pal = ""
        for idx in range(slen):
            pal1 = helper(idx, idx)  # Odd center
            pal2 = helper(idx, idx + 1)  # Even center

            longer_pal = pal1 if len(pal1) > len(pal2) else pal2
            if len(longer_pal) > len(longest_pal):
                longest_pal = longer_pal

        return longest_pal
