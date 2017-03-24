#!/usr/bin/python
# -*- coding: utf-8 -*-

from base.RandomList import IntList

class Solution(object):

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """"""
        """
        res = [0]*(num +1)
        exp2 = 1
        res[0] = 0
        for i in range(1, num +1):
            if i == exp2*2:
                res[i] = 1
                exp2 = i
            else:
                res[i] = res[i-exp2] + 1
        return res
    
    def multiplesThreeFive1(self, n):
        """
        Write a program that outputs the string representation of numbers from 1 to n.

        But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
        find multiples of 3, 5, and both respectively
        """

        d = ['Fizz', 'Buzz', 'FizzBuzz']
        
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append(d[2])
            elif i %5 == 0:
                res.append(d[1])
            elif i %3 == 0:
                res.append(d[0])
            else:
                res.append(str(i))
        return res

    def multiplesThreeFiveForce2(self, n):
        """
        
        """

        d = ['Fizz', 'Buzz', 'FizzBuzz']
        
        res = []
        for i in range(1, n+1):
            res.append(str(i))
        i = 3
        while(i <= n):
            res[i-1] = d[0]
            i += 3
        i = 5
        while(i <= n):
            res[i-1] = d[1]
            i += 5
        i = 15
        while(i <= n):
            res[i-1] = d[2]
            i += 15

        return res





def main():
    intList = IntList(1, 100).createNonDuplicateList(10, 1)
    sol = Solution()
    for nums in intList:
        print('input: ', nums[0])
        # print('output: ', Solution().countBits(nums[0]))
        print('FiveThree: ', Solution().multiplesThreeFive(nums[0]))
    

if __name__ == '__main__':
    main()

