# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, cur_sum = float('-INF'), 0
        for i in array:
            if cur_sum <= 0:
                cur_sum = i
            else:
                cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum
