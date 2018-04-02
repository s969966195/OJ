# -*- coding:utf-8 -*-


class Solution:
    data = []

    def Insert(self, num):
        # write code here
        if not self.data:
            self.data.append(num)
            return
        for i in range(len(self.data)):
            if self.data[i] >= num:
                self.data.insert(i, num)
                return
        self.data.append(num)

    def GetMedian(self, data):
        # write code here
        length = len(self.data)
        if length % 2 == 0:
            return (self.data[length/2] + self.data[length/2-1]) / 2.0
        else:
            return self.data[length/2]
