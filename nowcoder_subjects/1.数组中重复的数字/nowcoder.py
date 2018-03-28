# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) > 1:
                duplication[0] = numbers[i]
                return True

        return False


s = Solution()
s.duplicate([2, 1, 3, 1, 4], [])
