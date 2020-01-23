# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 2. DFS search, track 3 boolean vars at each search call: mid, left, right 
class Solution:
    def __init__(self):
        self.lca = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # DFS search 
        def search(node):
            if not node:
                return False
            
            mid = (node == q) or (node == p)
            left = search(node.left)
            right = search(node.right)
            # if curr == q, 
            if (mid + left + right) >= 2:
                print(".")
                self.lca = node
            return mid or left or right
        search(root)
        return self.lca
        

# 1. Record the visited paths to p, q
#    Then iterate the paths to find LCA
# Time limit exceeded
class SolutionBF:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def search(node, x, path):
            if not node:
                return []
            if node == x:
                return [node] + path
            return search(node.left, x, [node] + path) or search(node.right, x, [node] + path)
            

        path_to_p = search(root, p, [])
        path_to_q = search(root, q, [])
        
        #
        if path_to_p == [] or path_to_q == []:
            return None
        
        for i in path_to_p:
            if i in path_to_q:
                return i
            
        return lca