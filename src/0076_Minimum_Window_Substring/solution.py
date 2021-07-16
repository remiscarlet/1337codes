import collections


class Solution:
    """
    Does not pass all cases yet. Times out on extremely large inputs - particularly with many unique chars in 't'.

    Optimize `contains_all_chars()`
    """

    def minWindow(self, s: str, t: str) -> str:
        # "Naive"
        t_counter = collections.Counter(t)
        mapping_s = []  # Compressed idx to orig idx
        compressed_s = ""  # s but with only chars in t
        for idx, c in enumerate(s):
            if c in t_counter:
                mapping_s.append(idx)
                compressed_s += c

        def contains_all_chars(l, r) -> bool:
            # Too slow. Memoize/cache? Recounting long compressed_s strings hit timeout.
            sub_s_counter = collections.Counter(compressed_s[l : r + 1])
            for char in t_counter.keys():
                if char not in sub_s_counter or t_counter[char] > sub_s_counter[char]:
                    return False
            return True

        l = r = 0
        min_str_idxs, min_len = None, len(s)
        while r < len(compressed_s):
            # print(f"l:{l}, r:{r}, sub_s:{compressed_s[l:r+1]}")
            if not contains_all_chars(l, r):
                r += 1
            else:
                win_len = mapping_s[r] - mapping_s[l]
                # print(f"{win_len} < {min_len}")
                if win_len < min_len:
                    min_str_idxs, min_len = (l, r), win_len
                l += 1

        # print(f"{min_str_idxs}, {mapping_s}, {s}")
        if min_str_idxs is None:
            return ""
        else:
            l, r = min_str_idxs
            return s[mapping_s[l] : mapping_s[r] + 1]
