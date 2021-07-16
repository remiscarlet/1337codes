import collections
from typing import List, Tuple

UP = (-1, 0)
DOWN = (+1, 0)
LEFT = (0, -1)
RIGHT = (0, +1)


class History:
    def __init__(self):
        self.data = {}

    IS_WORD = "#"
    DID_EXIST = "@"

    def add(self, word: str):
        data = self.data
        for c in word:
            if c not in data:
                data[c] = {}
            data = data[c]
        data[self.IS_WORD] = True

    def set_found_state(self, word: str, did_exist: bool):
        self.add(word)

        data = self.data
        for c in word:
            data = data[c]
        data[self.DID_EXIST] = did_exist

    def is_prefix(self, prefix: str) -> bool:
        data = self.data
        for c in prefix:
            if c not in data:
                return False
            data = data[c]
        return True

    def did_exist(self, prefix: str) -> bool:
        data = self.data
        for c in prefix:
            if c not in data:
                return False
            data = data[c]
        return self.DID_EXIST in data


class Solution:
    """
    WIP. Does not pass.
    """

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        out_of_bounds = lambda row, col: row < 0 or row >= m or col < 0 or col >= n

        letter_pos = collections.defaultdict(set)
        for row in range(m):
            for col in range(n):
                c = board[row][col]
                letter_pos[c].add((row, col))

        history = History()
        for word in words:
            history.add(word)

        def search_word(pos: Tuple, prefix: str, suffix: str, visited: set) -> bool:
            if suffix == "":
                return True

            print(f"At:{pos}, prefix:{prefix}, suffix:{suffix}, visited:{visited}")
            nonlocal letter_pos, history
            row, col = pos
            assert board[row][col] == prefix[-1]

            if pos in visited:
                history.set_found_state(prefix, False)
                return False

            visited.add(pos)
            next_letter = suffix[0]
            for d_row, d_col in [UP, DOWN, LEFT, RIGHT]:
                new_row, new_col = row + d_row, col + d_col

                if (
                    out_of_bounds(new_row, new_col)
                    or (new_row, new_col) not in letter_pos[next_letter]
                    or not history.is_prefix(prefix + next_letter)
                ):
                    print(
                        f"newpos:({new_row},{new_col}), {board[new_row][new_col] if not out_of_bounds(new_row, new_col) else None} ,{history.is_prefix(prefix + next_letter)}-{prefix+next_letter}, {letter_pos[next_letter] if next_letter in letter_pos else None}"
                    )

                    continue

                if history.did_exist(prefix + next_letter) or search_word(
                    (new_row, new_col), prefix + next_letter, suffix[1:], visited
                ):
                    history.set_found_state(prefix, True)
                    return True

            visited.remove(pos)
            history.set_found_state(prefix, False)
            return False

        valid_words = []
        for word in words:
            for start_pos in letter_pos[word[0]]:
                if search_word(start_pos, word[0], word[1:], set()):
                    valid_words.append(word)
                    break

        return valid_words
