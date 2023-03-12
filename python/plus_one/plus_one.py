from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''
            Given a list with integers, increment the large integer by one and
            return the resulting array of digits.

            Parameters
            ----------
            digits: list
                List with integers.

            Returns
            -------
            plus_one_digits: list
                Array with digist incremented by one.
        '''
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
