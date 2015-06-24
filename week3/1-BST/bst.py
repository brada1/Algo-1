class BST:
    
    # Checks if a binary tree is a binary search tree.
    # root - node with 'left', 'right' and 'value' properties
    
    inf = float("infinity")
    ninf = float("-infinity")
    
    def isBST(root, minVal = ninf, maxVal = inf):
        '''based on simple recursion alongside check for validity'''
        if root is None:
            return True

        if not minVal <= root.value <= maxVal:
            return False

        return BST.isBST(root.left, minVal, root.value) and \
               BST.isBST(root.right, root.value, maxVal)



    def isBST2(root, lastNode = [ninf]):
        '''check if in-order traversal provides the nodes in proper sorted fashion'''
        if root is None:
            return True

        if not BST.isBST2(root.left, lastNode):
            return False

        if root.value < lastNode[0]:
            return False

        lastNode[0] = root.value
        return BST.isBST2(root.right, lastNode)
