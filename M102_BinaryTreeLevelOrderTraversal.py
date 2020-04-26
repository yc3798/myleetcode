# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # mid 
        # left, right 
        # ll, lr, rl, rr 
        # ...
        # use a Queue to store (node, level), when level increments, create new sublist 
        queue = [(root, 0)]
        res = []
        prev = 0 # depth 
        temp = []

        while queue != []:
            curr, level = queue.pop(0)
            # reset
            if level > prev: 
                prev = level
                res.append(temp)
                temp = []
                
            if curr: # check for None 
                temp.append(curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res
                
            
            
            
        