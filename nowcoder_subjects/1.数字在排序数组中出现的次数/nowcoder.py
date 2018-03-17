# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # return data.count(k)

        lenth = len(data)
        if lenth == 0:
            return 0
        firstK = self.getFirstK(data, k, 0, lenth-1)
        lastK = self.getLastK(data, k, 0, lenth-1)
        if firstK != -1 and lastK != -1:
            return lastK - firstK + 1
        return 0

    # 递归
    def getFirstK(self, data, k, start, end):
        if start > end:
            return -1
        mid = (start + end) >> 1  # 右移一位相当于除2
        if data[mid] > k or (mid-1 >= 0 and data[mid-1] == k):
            return self.getFirstK(data, k, start, mid-1)
        elif data[mid] < k:
            return self.getFirstK(data, k, mid+1, end)
        else:
            return mid

    # 循环
    def getLastK(self, data, k, start, end):
        length = len(data)
        mid = (start + end) / 2
        while start <= end:
            if data[mid] > k:
                end = mid-1
            elif data[mid] < k or (mid+1 < length and data[mid+1] == k):
                start = mid+1
            else:
                return mid
            mid = (start + end) / 2
        return -1


s = Solution()
print s.GetNumberOfK([1, 2, 3, 4, 1, 2, 1], 1)
