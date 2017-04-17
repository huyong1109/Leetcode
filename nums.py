from base.RandomList import IntList
class Solution(object):
    def find132pattern(self, nums):
        """
        Not done yet
        """
        if not nums:
            return False
        l = h = nums[0]
        for n in nums:
            if n <= l:
                l = n
            elif n >= h:
                h = n
            else:
                return True
        return False


    
    def threeSumForce(self, nums):
        
        if not nums:
            return []
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        return res
    
    def nextGreaterElement_force(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """"""
        """
        res  = []
        numsLen = len(nums)
        for m in findNums:
            i = 0
            while(nums[i] != m):
                i += 1
            while(i < numsLen and nums[i] <= m):
                i += 1
            if i >= numsLen:
                res.append(-1)
            else:
                res.append(nums[i])

        return res

    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """"""
        """
        numsLen = len(nums)
        res = {}
        vq = []
        for i in range(numsLen):
            while(vq and vq[-1] < nums[i]):
                res[vq.pop() ] = nums[i]
            vq.append(nums[i])


        return [res[v] if v in res else -1 for v in findNums]

    def nextGreaterElementIter(self, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """"""
        """
        numsLen = len(nums)
        res = [-1]*numsLen
        vq = []
        newNums = nums + nums[:-2]
        for i in range(len(newNums)):
            while(vq and nums[vq[-1]] < newNums[i]):
                res[vq.pop()] = newNums[i]
            if (i < numsLen):
                vq.append(i)

        return res

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """"""
        """
        if len(A) <= 2:
            return 0
        Arithmetrics = []
        diff = A[1] - A[0]
        curLen = 0 
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                curLen += 1
            else:
                if curLen > 0:
                    Arithmetrics.append(curLen)
                    curLen = 0
                diff = A[i] - A[i-1]
        if curLen >0:
            Arithmetrics.append(curLen)


        print Arithmetrics
        return sum([val*(val+1)/2 for val in Arithmetrics])
               
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        




def main():
    # intList = IntList(1, 20)
    # intLists = intList.createNonDuplicateList(20, 10)

    # for nums in intLists:
    #     print(nums)
    #     print('output: ', Solution().find132pattern(nums))
        # print('output: ', Solution().threeSumForce(nums))

        # subNums = intList.randomSampleList(nums)
        # print('input: ', subNums, nums)
        # print('output: ', Solution().nextGreaterElement_force(subNums, nums))
        # print('output: ', Solution().nextGreaterElement(subNums, nums))

        # print(nums, Solution().nextGreaterElementIter(nums))
    
    print(Solution().numberOfArithmeticSlices([1,2,3,4]) )

if __name__ == '__main__':
    main()

