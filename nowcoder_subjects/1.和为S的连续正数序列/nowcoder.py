# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # 等差序列求和
        # 根据数学公式计算:(a1+an)*n/2=s  n=an-a1+1
        # (an+a1)*(an-a1+1)=2*s=k*l(k>l)
        # an=(k+l-1)/2  a1=(k-l+1)/2
        res = []
        for i in range(1, tsum/2+1):
            for j in range(i, tsum/2+2):
                tmp = (j+i)*(j-i+1)/2
                if tmp > tsum:
                    break
                elif tmp == tsum:
                    res.append(range(i, j+1))
        return res


s = Solution()
s.FindContinuousSequence(100)
