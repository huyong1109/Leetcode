from __future__ import print_function
from base.RandomList import StringList
import timeit

"""
Given a string, find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubString(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLen = 0
        length = len(s)
        curStr = {}
        high = 0
        low = 0

        while(high < length):
            c = s[high]
            if c in curStr:
                low = max(low, curStr[c] + 1)
            curStr[c] = high
            maxLen = max(maxLen, high - low +1)
            high += 1
            # print( c, maxLen)
        return maxLen

    def lengthOfLongestSubStringIndex(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxLen = 0
        length = len(s)
        index = [-1]*256
        high = 0
        low = 0

        for high in range (length):
            c = ord(s[high])
            low = max(low, index[c] + 1)
            index[c] = high
            maxLen = max(maxLen, high - low +1)
            # print( c, maxLen)
        return maxLen


def test(function, size, length):
    stringObj = StringList(2)
    stringList = stringObj.createRandomString(size, length)
    sol = Solution()
    for testStr in stringList:
        if function == 0:
            print(testStr, sol.lengthOfLongestSubString(testStr))
        elif function ==1:
            print(testStr, sol.lengthOfLongestSubStringIndex(testStr))


def main():
    time2 = timeit.Timer("test(1, 10, 200)", setup='from __main__ import test')
    time1 = timeit.Timer("test(0, 10, 200)", setup='from __main__ import test')

    print('Method 1', time1.timeit(1))
    print('Method 2', time2.timeit(1))

if __name__ == '__main__':
    main()
