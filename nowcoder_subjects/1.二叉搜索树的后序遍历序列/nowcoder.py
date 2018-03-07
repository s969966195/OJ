# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        lenth = len(sequence)
        if lenth == 0:
            return False

        if lenth == 1:
            return True

        root = sequence[-1]
        left = 0

        while sequence[left] < root:
            left += 1

        for j in range(left, lenth-1):
            if sequence[j] < root:
                return False

        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:lenth-1])


s = Solution()
print s.VerifySquenceOfBST([4,8,6,12,16,14,10])
