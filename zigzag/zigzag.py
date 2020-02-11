class ZigZag(object):
    def convert(self, s, numRows):
        s = str(s)
        res = [[] for i in range(numRows)]
        res_str = ""
        zig = numRows * 2 - 2
        if numRows >= len(s) or numRows == 1:
            return s
        for i in range(len(s)):
            numberOfRow = i % zig if i % zig < numRows else zig - i % zig
            res[numberOfRow].append(s[i])
        for i in range(numRows):
            res_str += ''.join(res[i])
        return res_str
