class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr = list(str(x))
        for i in range(len(arr)):
            if arr[i] != arr[-i-1]:
                return False
        return True
