# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        while 0 in numbers:
            numbers.remove(0)
        ma = max(numbers)
        mi = min(numbers)
        setnumbers = set(numbers)
        if len(numbers) != len(setnumbers):
            return False
        if ma - mi <= 4:
            return True
        return False


s = Solution()
print s.IsContinuous([0, 1, 0, 2, 3])
