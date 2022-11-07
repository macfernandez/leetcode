from typing import List


class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        plus_one_digits = list()
        to_add = 1
        for d in digits[::-1]:
            if to_add:
                if d==9:
                    plus_one_digits.insert(0, 0)
                else:
                    plus_one_digits.insert(0, d+to_add)
                    to_add = 0
            else:
                plus_one_digits.insert(0, d)
        if to_add:
            plus_one_digits.insert(0, 1)
        return plus_one_digits
