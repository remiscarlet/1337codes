from typing import List, Tuple


class Solution:
    """
    Naive af
    Runtime: 31.92%
    Memory: 6.98%
    """

    def parse(self, start_idx: int) -> Tuple[int, List]:
        vals: List = []
        acc = ""
        resume_idx = -1
        idx = start_idx
        while idx < self.slen:
            c = self.s[idx]
            if c.isdigit():
                acc += c
            else:
                if acc != "":
                    vals.append(int(acc))
                    acc = ""

                if c in "+-":
                    vals.append(c)
                elif c in "(":
                    idx, sub_vals = self.parse(idx + 1)
                    vals.append(sub_vals)
                    continue
                elif c in ")":
                    resume_idx = idx + 1
                    break
                else:
                    raise RuntimeError()
            idx += 1

        if acc != "":
            vals.append(int(acc))

        return resume_idx, vals

    def interpret(self, vals: List):
        final_sum = 0
        is_negative = False
        for val in vals:
            if type(val) == int:
                final_sum += (-1 if is_negative else +1) * val
                is_negative = False
            elif type(val) == list:
                final_sum += (-1 if is_negative else +1) * self.interpret(val)
                is_negative = False
                pass
            elif val == "-":
                is_negative = True
        return final_sum

    def calculate(self, s: str) -> int:
        s = "".join([c for c in s if c != " "])
        self.s = s
        self.slen = len(s)
        # print(self.s, self.slen)

        _, vals = self.parse(0)
        # print(vals)

        return self.interpret(vals)
