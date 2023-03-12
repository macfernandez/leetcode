class Solution:
    def length_of_last_word(self, s: str) -> int:
        '''
            Given string s consisting of words and spaces, return the length of
            the last word in the string.


            Parameters
            ----------
            s: str
                String of words and spaces.

            Returns
            -------
            last_word_length: int
                Length of the last word in the string.
        '''
        last_word = s.strip().split()[-1]
        last_word_length = len(last_word)
        return last_word_length
