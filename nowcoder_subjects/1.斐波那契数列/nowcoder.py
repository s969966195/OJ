# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        a, b, c = 0, 1, 1
        i = 2
        while i < n:
            a, b = b, c
            c = a + b
            i += 1
        return c


s = Solution()
print s.Fibonacci(3)
