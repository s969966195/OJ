# -*- coding:utf-8 -*-
import collections


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        '''
        if len(numbers) == 1:
            return numbers[0]
        newnumbers = sorted(numbers)
        temp = 1
        for i in range(1, len(newnumbers)):
            if newnumbers[i] != newnumbers[i-1]:
                temp = 1
            else:
                temp += 1

            if temp > len(newnumbers) / 2:
                return newnumbers[i]

        return 0
        '''
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k

        return 0


s = Solution()
print s.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2])
