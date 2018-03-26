# -*- coding:utf-8 -*-
class Solution:

    res = 0

    def Sum_Solution(self, n):
        # write code here
        # return sum(range(1, n+1))

        '''
        # &&就是逻辑与，逻辑与有个短路特点，前面为假，后面不计算。
        ans = n
        ans && (ans += self.Sum_Solution(n - 1))
        return ans
        '''
        def calsum(n):
            self.res += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        calsum(n)
        return self.res
