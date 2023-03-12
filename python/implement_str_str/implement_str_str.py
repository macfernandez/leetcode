class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
            Find first occurrence index of needle in haystack.

            Parameters
            ----------
            haystack: str
                Haystack string.

            needle: str
                Needle string.

            Returns
            -------
            solution: int
                First occurrence index of needle in haystack.
        '''
        if needle != '':
            if needle in haystack:
                len_needle = len(needle)
                for i in range(len(haystack)):
                    if haystack[i:i+len_needle] == needle:
                        solution = i
                        break
            else:
                solution = -1
        else:
            solution = 0
        return solution
