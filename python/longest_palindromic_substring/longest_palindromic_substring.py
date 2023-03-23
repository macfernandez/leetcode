class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _longesPalindrome(p):
            palindrome = ''
            while palindrome == '':
                if len(p) % 2:
                    mid = len(p)//2
                    for i in range(mid):
                        i += 1
                        if p[mid-i] == p[mid+i]:
                            palindrome = p[mid-i:mid+i+1]
                        else:
                            break
                else:
                    mid = len(p)//2
                    for i in range(mid):
                        if p[mid-(i+1)] == p[mid+i]:
                            palindrome = p[mid-(i+1):mid+(i+1)]
                        else:
                            break
                p = p[:-1]
            return palindrome
        if len(s) > 1:
            forward = _longesPalindrome(s)
            backward = _longesPalindrome(s[::-1])
            longest = forward if len(forward) > len(backward) else backward
        else:
            longest = s
        return longest
