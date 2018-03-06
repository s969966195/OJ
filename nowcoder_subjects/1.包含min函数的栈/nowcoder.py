# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]

s = Solution()
s.push(5)

s.push(4)
s.push(3)
s.push(8)
s.push(10)
s.push(11)
s.push(12)
s.push(1)
print s.pop()
print s.pop()
