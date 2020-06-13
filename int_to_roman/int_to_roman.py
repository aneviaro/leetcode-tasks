class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        enum = {1: 'I', 4:'IV',5: 'V', 9:'IX',10: 'X', 40:'XL',50: 'L', 90:'XC' ,100: 'C', 400: 'CD', 500: 'D', 900:'CM', 1000: 'M'}
        res = ''
        enum_keys = sorted(enum.keys(), reverse=True)
        for i in range(len(enum_keys)):
            key=enum_keys[i]
            while num>=key:
                num-=key
                res+=''.join(enum.get(key))
        return res
