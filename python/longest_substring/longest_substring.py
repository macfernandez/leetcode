class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = len(set(s))
        stop = False
        if max_length != len(s):
            i = 0
            while (max_length != 0) and (not stop):
                max_length -= i
                for start in range(0, len(s)-max_length+1):
                    substring = s[start: start+max_length]
                    substring_length = len(set(substring))
                    print(start, start+max_length, ':', s[start: start+max_length], substring_length)
                    if substring_length == max_length:
                        stop = True
                        break
                i = 1
        return max_length
