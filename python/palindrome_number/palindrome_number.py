# problem 9
# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
            Take an integer and return if it is a palindrome.

            Parameters
            ----------
            x: int
                Integer.

            Returns
            -------
            solution: bool
                True if it is a palindrome, False otherwise.
        '''
        number, reverse = x, 0
        while 0 < x:
            remainder = x%10
            reverse = (reverse*10) + remainder
            x = int((x-remainder)/10)
        return number == reverse