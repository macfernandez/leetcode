class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        while palindrome == '':
            if len(s) % 2:
                mid = len(s)//2
                for i in range(mid):
                    i += 1
                    if s[mid-i] == s[mid+i]:
                        palindrome = s[mid-i:mid+i+1]
                    else:
                        break
            else:
                mid = len(s)//2
                for i in range(mid):
                    if s[mid-(i+1)] == s[mid+i]:
                        palindrome = s[mid-(i+1):mid+(i+1)]
                    else:
                        break
            s = s[:-1]
        return palindrome


s = ["nnabba", "abbaa", "babad", "cbbd"]
for _ in s:
    print('===>', _)
    print(Solution().longestPalindrome(_))