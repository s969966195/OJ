# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        '''
        while exponent != 0:
            if exponent & 1 == 1:
                res *= base
            base *= base
            exponent >>= 1
        '''
        return pow(base, exponent)
