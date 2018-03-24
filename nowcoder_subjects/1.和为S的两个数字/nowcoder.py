# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 设头尾两个指针
        # 两数相差越远乘积越小
        res = []
        lenth = len(array)
        i, j = 0, lenth-1
        while i < j:
            if array[i] + array[j] == tsum:
                res.append(array[i])
                res.append(array[j])
                break
            while i < j and array[i] + array[j] > tsum:
                j -= 1
            while i < j and array[i] + array[j] < tsum:
                i += 1
        return res


s = Solution()
print s.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15)
