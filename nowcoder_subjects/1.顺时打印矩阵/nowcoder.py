# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 魔方逆时针旋转
        res = []
        while matrix:
            res += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res

    def turn(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        newmatrix = []
        for i in range(col):
            newmatrix2 = []
            for j in range(row):
                newmatrix2.append(matrix[j][i])
            newmatrix.insert(0, newmatrix2)
        return newmatrix


s = Solution()
print s.printMatrix([[1]])

'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        if n==1 and m==1:
            res=[matrix[0][0]]
            return res
        for o in xrange((min(m,n)+1)//2):
            [res.append(matrix[o][i]) for i in xrange(o,m-o)]
            [res.append(matrix[j][m-1-o]) for j in xrange(o,n-o) if matrix[j][m-1-o] not in res]
            [res.append(matrix[n-1-o][k]) for k in xrange(m-1-o,o-1,-1) if matrix[n-1-o][k] not in res]
            [res.append(matrix[l][o]) for l in xrange(n-1-o,o-1,-1) if matrix[l][o] not in res]
        return res
'''
