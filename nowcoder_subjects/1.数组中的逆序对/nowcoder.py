# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here

        #
        # O(n^2) 遍历一遍
        #
        num = 0
        for i in range(1, len(data)):
            if data[i] < data[i-1]:
                num += 1
        return num % 1000000007
