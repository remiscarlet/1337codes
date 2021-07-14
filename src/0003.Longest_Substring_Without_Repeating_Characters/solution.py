class Solution:
    """
    Runtime: 98.86%
    Memory: 93.02%
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_so_far = ""
        curr = ""
        for c in s:
            if c not in curr:
                curr += c
            else:
                if len(curr) > len(longest_so_far):
                    longest_so_far = curr

                curr = curr[curr.index(c) + 1 :] + c

        if len(curr) > len(longest_so_far):
            longest_so_far = curr

        return len(longest_so_far)
