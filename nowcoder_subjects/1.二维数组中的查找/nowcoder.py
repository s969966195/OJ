# coding=utf-8
'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递
增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含
有该整数。
'''


def find(array, target):
    if len(array) == 1:
        if array[0] == target:
            return True
        else:
            return False
    middle = (len(array) - 1) / 2
    if target == array[middle]:
        return True
    elif target < array[middle]:
        return find(array[:middle+1], target)
    else:
        return find(array[middle+1:], target)


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target < array[0][0]:
            return False
        for arr in array:
            if target == arr[0] or ((target > arr[0]) and find(arr, target)):
                return True
        return False


s = Solution()
print s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
'''

a = [1, 2, 3, 4, 5]
print len(a) / 2
print a[:1]
'''
