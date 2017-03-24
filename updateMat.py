from __future__ import print_function
from base.Matrix import Matrix
import random
import timeit
import sys


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        ""
        """
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        dist = matrix
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    q.append((i,j))
        print(q)
        while(q):
            # tmpmat = [[e for e in row] for row in dist]
            dist = matrix
            qind = 0 
            while(qind < len(q)):
                i,j = q[qind]
                minus = dist[i][j]
                if i > 0:
                    minus = min(minus, dist[i-1][j])
                if i <m-1:
                    minus = min(minus, dist[i+1][j])
                if j > 0:
                    minus = min(minus, dist[i][j-1])
                if j <n-1:
                    minus = min(minus, dist[i][j+1])
                # print(i,j, minus)
                if minus >= dist[i][j]:
                    matrix[i][j] += 1
                    # print(i,j, tmpmat[i][j])
                    qind +=1
                else:
                    q.remove(q[qind])
                    # print(qind, 'removed')
            print('--------------')
            # dist =  [[e for e in row] for row in tmpmat]
            Matrix(matrix).printMat()
        return matrix

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        if not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        island = 0
        connet = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island += 1
                    if (i < m-1 and grid[i+1][j] ==1):
                        connet += 1
                    if (j <n-1 and grid[i][j+1] ==1):
                        connet += 1
        return 4*island - 2*connet
                
                



def main():
    mat = Matrix()
    matrix = mat.createRandomMat(8, 8, [0,1])
    sol = Solution()
    mat.printMat()
    # print(sol.updateMatrix(matrix))
    matrix = [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    print(sol.islandPerimeter(matrix))

if __name__ =='__main__':
    main()


                    
