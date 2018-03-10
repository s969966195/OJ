# -*- coding:utf-8 -*-
import itertools


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []

        # return sorted(list(set(map(''.join, itertools.permutations(ss)))))
        self.vis = [0 for i in range(len(ss))]
        self.res = []
        self.temp = ""
        self.DFS(0, ss)
        return sorted([i for i in set(self.res)])

    def DFS(self, su, ss):
        if su == len(ss):
            self.res.append(self.temp)
            return
        for i in range(len(ss)):
            if self.vis[i] == 0:
                self.vis[i] = 1
                self.temp += ss[i]
                self.DFS(su+1, ss)
                self.temp = self.temp[:-1]
                self.vis[i] = 0


s = Solution()
s.Permutation(['a', 'b', 'c'])
