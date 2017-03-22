from base.RandomList import IntList

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """"""
        """
        p1 = p2 = 0
        p = 0 
        len1, len2 = len(nums1), len(nums2)
        print(nums1, nums2)
        mid, odd = divmod(len1 + len2, 2) 
        sortlist= []
        while(p < mid + 1):
            if p1 < len1 and p2 < len2:
                if nums1[p1] <= nums2[p2]:
                    sortlist.append(nums1[p1])
                    p1 += 1
                else:
                    sortlist.append(nums2[p2])
                    p2 += 1
            elif p1 >= len1:
                if p2 < len2:
                    sortlist.append(nums2[p2])
                    p2 += 1
                else:
                    break
            else:
                sortlist.append(nums1[p1])
                p1 += 1
            p += 1
        if len(sortlist) == 0:
            return 0.0
        elif len(sortlist) ==1:
            return sortlist[0]
        else:
            if odd == 0:
                return sum(sortlist[-2:])/2.0
            else:
                return sortlist[-1]

    def findMedianSortedArraysBinarySearch(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """"""
        """
        n, m = len(nums1), len(nums2)
        if m > n: 
            n, m, nums1, nums2 = m, n, nums2, nums1
        if n <= 0:
            return 0
        if m <=0:
            return (nums1[n/2] + nums1[(n-1)/2])/2.0
        mid = (n+m +1)/2 
        imin, imax = 0, m
        while(imin <= imax):
            i = (imin + imax)/2
            j = mid - i
            if i<m and nums2[i] < nums1[j-1]:
                imin = i +1
            elif i >0 and nums2[i -1] > nums1[j]:
                imax = i -1
            else:
                if i == 0: maxl = nums1[j-1]
                elif j == 0: maxl = nums2[i-1]
                else: maxl = max(nums1[j-1], nums2[i-1])
                if (m+n)%2 != 0:
                        return maxl

                if i == m: minr = nums1[j]
                elif j == n: minr = nums2[i]
                else: minr = min(nums1[j], nums2[i])
                return (maxl + minr)/2.0


    def findMedianSortedArraysIterative(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """"""
        """
        n, m = len(nums1), len(nums2)

        return (self.findKthSortedArrays(nums1, nums2,(n+m)/2) + self.findKthSortedArrays(nums1, nums2,(n+m-1)/2))/2.0

    def findKthSortedArrays(self, nums1, nums2, k):
        """
        find the k th large number in two sorted arrays
        """
        print(nums1, nums2, k)
        n, m = len(nums1), len(nums2)
        if len(nums1) == 0 and len(nums2) == 0: 
            return 0
        if len(nums1) == 0:
            return nums2[k]
        elif len(nums2) == 0:
            return nums1[k]
        if k ==0:
            return min(nums1[0], nums2[0])
        m1 = min(n, k/2)
        m2 = min(m, k/2)
        if nums1[m1] < nums2[m2]:
            self.findKthSortedArrays()



def main():
    intList = IntList(1, 100).createNonDuplicateList(20, 10, sort=True)
    intList += [[1], [1], [], [], [], [1], [1,3], [2], [1,3], [2,4]]

    print(intList)
    for i in range(len(intList)/2):
        print('solution1 : ', Solution().findMedianSortedArrays(intList[2*i], intList[2*i+1]))
        print('solution2 : ', Solution().findMedianSortedArraysBinarySearch(intList[2*i], intList[2*i+1]))
        print('solution2 : ', Solution().findMedianSortedArraysIterative(intList[2*i], intList[2*i+1]))
    

if __name__ == '__main__':
    main()
