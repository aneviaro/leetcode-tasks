class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        char_ord_array = [x for x in range(48, 58)]
        plus_minus = [43, 45]
        str = str.strip()
        if len(str) == 0:
            return 0
        result_str = ""
        if ord(str[0]) not in char_ord_array and ord(str[0]) not in plus_minus:
            return 0
        else:
            result_str += str[0]
            str = str[1:]
        for char in str:
            if ord(char) in char_ord_array:
                result_str += char
            else:
                break
        #Check for int32
        try:
            if abs(int(result_str)) > (1 << 31) - 1:
                return -(1 << 31) if result_str[0] == "-" else (1 << 31)-1
            return int(result_str)
        except:
            return 0
