# -*- coding:utf-8 -*-
import heapq


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        '''
        stinput = sorted(tinput)
        return stinput[:k]
        '''
        # 堆
        heapq.heapify(tinput) # 数组变堆
        return [heapq.heappop(tinput) for _ in xrange(k)] # 弹出最小值
