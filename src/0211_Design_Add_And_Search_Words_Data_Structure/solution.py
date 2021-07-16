from typing import Optional, Dict


class WordDictionary:
    """
    Runtime: 68.82% - I think I have to use a non-recursive approach for >80%ile
    Memory: 83.95%
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def addWord(self, word: str) -> None:
        # print(f"Adding: {word}")
        data = self.data
        for c in word:
            if c not in data:
                data[c] = {}
            data = data[c]
        data["is_word"] = True

    def search(self, word: str) -> bool:
        def search_helper(word: str, data: Dict) -> bool:
            # print(f"word:{word}, data:{data}")
            for idx, c in enumerate(word):
                if c not in data:
                    if c == ".":
                        for key, sub_data in data.items():
                            if key == "is_word":
                                continue
                            if search_helper(word[idx + 1 :], sub_data):
                                return True
                    return False
                data = data[c]
            return "is_word" in data

        return search_helper(word, self.data)
