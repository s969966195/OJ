# -*- coding:utf-8 -*-


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""

        num = map(str, numbers)
        num.sort(lambda x, y: cmp(x+y, y+x))  # sort可以自定义比较函数
        return ''.join(num)


s = Solution()
s.PrintMinNumber([3, 32, 321])
