class Solution(object):
    def lengthOfLongestSubstring(self, s):
        b = []
        a = []
        k = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[i] not in a:
                k += 1
                a.append(s[i])
            else:
                a = list(s[s.index(s[i], i - k) + 1:i + 1])
                b.append(k)
                k = len(a)
        if k != 0:
            b.append(k)
        return max(b)
