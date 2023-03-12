class Solution:
    def isValid(self, s: str) -> bool:
        '''
            Take a string with parentheses ('()[]{}') and return True if all
            brackets are open and closed in the correct order by the same type.
            In other case return False.

            Parameters
            ----------
            s: str
                String with parentheses.

            Returns
            -------
            valid: bool
                True if valid, False if not.
        '''
        queue = list()
        for i in range(len(s)):
            if len(queue)==0:
                queue.append(s[i])
            else:
                if queue[-1]+s[i] in ['()','[]','{}']:
                    queue = queue[:-1]
                else:
                    queue.append(s[i])
        valid = True if len(queue)==0 else False
        return valid
