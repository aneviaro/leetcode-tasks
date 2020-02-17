class Solution(object):
    def reverse(self, x):

        """
        :type x: int
        :rtype: int
        """

        if abs(x) > (1 << 31) - 1:
            return 0
        else:
            revers_str = "".join(list(reversed(list(str(abs(x))))))
            revers_int = int(revers_str) if int(revers_str) < ((1 << 31) - 1) else 0
            if x < 0:
                return -revers_int
            return revers_int
