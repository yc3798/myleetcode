# 1/15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Inorder: left, mid, right
# preorder: mid, left, right
# postorder: left, right, mid

# Recursive: trivial O(n)
# Iterative: use a stack and a list 
# initialize stack = [root]
# while stack: pop from stack, if the item is a TreeNode, push back (right, curr.val, left)
# if the item is an integer(value), append this value to list 
class Solution:
    def inorderTraversalRec(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        return self.traverse(root, [])

    def traverse(self, root, ans):
        if not root:
            return ans
        ans = self.traverse(root.left, ans)
        ans.append(root.val)
        return self.traverse(root.right, ans)


    # iterative:
    def inorderTraversal(self, root):
        ans = []
        if not root:
            return []
        stack = [root]
        while stack:
            curr = stack.pop(0)
            if type(curr) == int:
                ans.append(curr)
            elif curr is not None: # this is a tree node, push back righttree, root.val, lefttree
                stack.insert(0, curr.right)
                stack.insert(0, curr.val)
                stack.insert(0, curr.left)
        print(ans)



