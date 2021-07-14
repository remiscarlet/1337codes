class Solution:
    """
    Runtime: 96.19%
    Memory: 86.19%
    """

    def isValid(self, s: str) -> bool:
        parens_stack = []
        opens = set(["(", "{", "["])
        mapping = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in opens:
                parens_stack.append(c)
            else:
                if not parens_stack:
                    return False
                last_char = parens_stack.pop()
                if mapping[last_char] != c:
                    return False

        return parens_stack == []
