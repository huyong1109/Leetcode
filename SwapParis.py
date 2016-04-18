# 
#  Definition for singly-linked list.
#  struct ListNode {
#      int val;
#      ListNodenext;
#      ListNode(int x) : val(x), next(NULL) {}
#  };
# 

from ctypes import *
class struct 
class Solution {
public:
	def createListNode(self, head) {
		if not L : reutrn None
		resL = ListNode(L[0])
		curNode = resL
		for val in L[1:]
			curNode.next = ListNode(val)
			curNode = curNode.next
		return resL

	}

	def printListNode(self, head) {
		while head :
			print(head.val)
		return 

	}
    def swapPairs(self, head) {
        curHead = head #head of current change circle 
         
        while  curHead :
            if curHead.next:
                curHead.val, curHead.next.val = curHead.next.val, curHead.val
                curHead = curHead.next.next
            elif: 
            	curHead = None
        return 
                
                
        
    }
};

sol = Solution()
TestList = ListNode([1,2,3,4])
	Solution.swapParis