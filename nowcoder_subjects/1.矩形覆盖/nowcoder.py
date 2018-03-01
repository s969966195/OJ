# -*- coding:utf-8 -*-


class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 3:
            return number
        else:
            a, b = 2, 3
            i = 3
            while i < number:
                a, b = b, a+b
                i += 1
            return b
