from __future__ import print_function 
from base.Struct import ListNode


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


def main():
    testList = range(6)
    sol = Solution()
    print(testList)
    testListNode = sol.createListNode(testList)
    newListNode = sol.swapPairs(testListNode) 
    print('SwapPairs')
    sol.printListNode(newListNode)

if __name__ == '__main__':
    main()
