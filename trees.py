from base.Struct import BinaryTree

class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None
        nodeQ = [root]
        while(nodeQ):
            childQ = []
            res = nodeQ[0].val
            for node in nodeQ:
                if node.left: childQ.append(node.left)
                if node.right: childQ.append(node.right)
            nodeQ = childQ
        return res



def main():
    sol = Solution()
    tree = BinaryTree([2,1,3,None,4, 4])
    print('serilized', tree.serialized)
    print(tree.serialized)
    tree.printTree()
    print(sol.findBottomLeftValue(tree.head))

if __name__ == '__main__':
    main()

