class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        enum = {'I':1, 'IV':4,'V':5, 'IX':9,'X':10, 'XL':40, 'L':50, 'XC':90 , 'C':100,  'CD':400,  'D':500, 'CM':900,  'M':1000}
        res = 0
        enum_keys = sorted(enum.keys(), reverse=True)
        i=0
        while i < len(s):
            if s[i] in ('I', 'X', 'C') and i<len(s)-1:
                tmp = s[i]+s[i+1]
                if tmp in enum_keys:
                    res+=enum.get(tmp)
                    i+=2
                    continue
                else:
                    res+=enum.get(s[i])
                    i+=1
                    continue
            else:
                res+=enum.get(s[i])
                i+=1
        return res


