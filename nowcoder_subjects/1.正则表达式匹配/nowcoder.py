# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        slength = len(s)
        plength = len(pattern)
        if slength == 0 and plength == 0:
            return True
        if slength > 0 and plength == 0:
            return False
        if plength > 1 and pattern[1] == '*':
            if slength > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if slength > 0 and (pattern[0] == '.' or pattern[0] == s[0]):
            return self.match(s[1:], pattern[1:])
        return False
