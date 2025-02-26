# problem 13
# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        '''
            Take a roman number and return it as integer.

            Parameters
            ----------
            s: str
                Roman number.

            Returns
            -------
            solution: int
                Integer.
        '''
        roman2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        solution = 0
        queue = [0]
        for i in s:
            int_n = roman2int.get(i)
            if int_n < queue[-1]:
                solution += sum(queue)
                queue = [int_n]
            elif int_n == queue[-1]:
                queue.append(int_n)
            else:
                int_n -= sum(queue)
                queue = [int_n]
        solution += sum(queue)
        return solution
