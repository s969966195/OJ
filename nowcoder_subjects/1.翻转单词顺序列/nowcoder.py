# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        # return ' '.join(list(reversed(s.split(' '))))
        slist = s.split(' ')
        res = []
        for i in range(len(slist)-1, -1, -1):
            res.append(slist[i])
        return ' '.join(res)


s = Solution()
print s.ReverseSentence("student. a am I")
