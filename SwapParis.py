# 
#  Definition for singly-linked list.
#  struct ListNode {
#      int val;
#      ListNodenext;
#      ListNode(int x) : val(x), next(NULL) {}
#  };
# 


class ListNode(object):
	def __init__(self, val):
		self.val = val 
		self.next = None 


class Solution(object):
	def createListNode(self, L):

		if not L : 
			print('input Null')
			return None
		resL = ListNode(L[0])

		curNode = resL
		for val in L[1:]:

			curNode.next = ListNode(val)
			curNode = curNode.next
		self.printListNode(resL)
		return resL
		

	def printListNode(self, head):
		print("List:  [", end="")
		while head.next :
			print(head.val, end=",")
			head = head.next
		print(head.val, end="")
		print("]")
		return 

	def swapPairs(self, head) :

		p1 = guard = ListNode(0)
		guard.next = head

		try:
			while True:
				p0, p1, p2 = p1, p1.next, p1.next.next
				p0.next, p1.next, p2.next = p2, p2.next, p1
		except:
			return guard.next
testList = range(6)
sol = Solution()
print(testList)
testListNode = sol.createListNode(testList)
newListNode = sol.swapPairs(testListNode) 
print('SwapPairs')
sol.printListNode(newListNode)