# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        length = len(A)
        B = [None for i in range(length)]
        # 前半部分
        B[0] = 1
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]
        # 后半部分
        tmp = 1
        for i in range(length-2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B



s = Solution()
s.multiply([0, 1, 2, 3, 4])
