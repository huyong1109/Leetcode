### Define all the structures here for 


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

    def printNode(self):
        print('ListNode value: ', self.val)


class BinaryNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def printNode(self):
        print('BinaryNode value: ', self.val)

# Definition for SingleList
class SingleLink(ListNode):
    def __init__(self,serialized=None):
        if not serialized:
            serialized = []
        self.serialized = serialized
        self.head = self.deserialize(serialized)

    def deserialize(self, serialized):
        if not serialized:
            return None
        head = ListNode(serialized[0])
        node = head
        for val in serialized[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

    def appendNode(self, node):
        if not isinstance(node, ListNode):
            node = ListNode(node)
        endNode = self.getEndNode()
        if not endNode:
            self.head = node
        else:
            self.getEndNode().next = node


    def getEndNode(self):
        endNode = self.head
        while(endNode.next):
            endNode = endNode.next
        return endNode
    
    def serialize(self):
        self.serialized = []
        node = self.head
        while(node):
            self.serialized.append(node.val)
            node = node.next
        return

    
    def printLink(self):
        self.serialize()
        printStr = [str(val) for val in self.serialized]
        print('->'.join(printStr))
         

    def test(self):
        testLink = SingleLink([0, 1, 2])
        testLink.printLink()
        testLink.getEndNode().printNode()
        testLink.appendNode(3)
        print('append value 3')
        testLink.printLink()
        print('append ListNode(4)')
        testLink.appendNode(ListNode(4))
        testLink.printLink()




# Definition for a binary tree node.
class BinaryTree(BinaryNode):
    def __init__(self, serialized=None):
        self.serialized = serialized 
        self.height = None
        self.head = self.deserialize(serialized)

    def deserialize(self, serialized):
        if not self.serialized:
            return None
        nodes = [None if val == None else BinaryNode(val) 
                 for val in serialized]
        kids = nodes[::-1]
        head = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return head

    def serialize(self):
        if not self.head:
            self.height = 0
            return []
        self.serialized = []
        nodeQ = [self.head]
        self.serialized.append(self.head.val)
        self.height = 1
        while(nodeQ):
            self.height += 1
            childQ = []
            for node in nodeQ:
                if node:
                    self.serialized.append(node.left.val)
                    self.serialized.append(node.right.val)
                    if node.left:   childQ.append(node.left)
                    if node.right:  childQ.append(node.right)
            nodeQ = childQ
        return 

    def printTree(self):

        def printTreeNode(node, level=0):
            if node:
                if level == 0:
                    print(str(node.val))
                else:
                    print('\t'*(level -1) + '|'+'-'*7 + str(node.val))
                if not node.right and node.left:
                    print('\t'*(level) + '|')
                printTreeNode(node.right, level+1)
                printTreeNode(node.left, level+1)
        printTreeNode(self.head)
        


                





