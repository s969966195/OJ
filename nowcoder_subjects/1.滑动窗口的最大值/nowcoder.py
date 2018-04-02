# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        length = len(num)
        if not num or size < 1 or length < size:
            return []
        res = []
        i = size
        while i <= length:
            res.append(max(num[i-size:i]))
            i += 1
        return res


s = Solution()
print s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
