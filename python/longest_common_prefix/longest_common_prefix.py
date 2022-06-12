from typing import *

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        '''
            Given a list with strings, return the common prefix for those
            elements.

            Parameters
            ----------
            strs: list
                List with strings.

            Returns
            -------
            solution: str
                Common prefix for the strings in list. If there is no shared
                prefix, '' is returned.
        '''
        solution = ''
        for i in range(1,len(strs[0])+1):
            prefix = strs[0][:i]
            if all([s.startswith(prefix) for s in strs]):
                solution = strs[0][:i]
        return solution
