# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        # self.sdict = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.s.count(i) == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s = self.s + char
        '''
        if char in self.sdict:
            self.sdict[char] = self.sdict[char] + 1
        else:
            self.sdict[char] = 1
        '''
