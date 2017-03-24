from __future__ import print_function
from base.RandomList import StringList
import random
import timeit
import sys

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for c in magazine:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for c in ransomNote:
            if c in d and d[c] >= 1:
                d[c] -= 1
            else:
                return False

        return True


    def isSubString(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in xrange(len(magazine)):
            j = 0
            while(j < len(ransomNote)):
                if  ransomNote[j] != magazine[i+j]:
                  break
                j += 1
            if j == len(ransomNote):
                  return True
        
        return False

def main():
    stringObj = StringList(2)
    stringList = stringObj.createRandomString(20, 20) 
    sol = Solution()
    for i in range(len(stringList)/2):
        str1 = stringList[2*i]
        str2 = stringList[2*i+1]
        flag = False
        if random.random() > 0.5:
            str1 = stringObj.randomSubString(str2)
            flag = True
        print(str1, str2, flag, sol.canConstruct(str1, str2))

if __name__ =='__main__':
    main()


                    
                  
