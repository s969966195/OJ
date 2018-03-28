# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        '''
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) > 1:
                duplication[0] = numbers[i]
                return True

        return False
        '''
        # 因为题目里写了数组里数字在0 ~ n-1 之间，所以可以利用现有数组设置标志，当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。
        length = len(numbers)
        for i in range(length):
            index = numbers[i]
            if index >= length:
                index -= length
            if numbers[index] >= length:
                duplication[0] = index
                return True
            numbers[index] = numbers[index] + length
        return False


s = Solution()
s.duplicate([2, 1, 3, 1, 4], [])
