class Solution:
    def length_of_last_word(self, s: str) -> int:
        last_word = s.strip().split()[-1]
        length_last_word = len(last_word)
        return length_last_word
        