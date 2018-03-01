# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]
        return rotateArray[0]
