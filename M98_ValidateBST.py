# T(n) =  
import sys
class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def findmin(self,v):
        """find min from binary tree"""
        if v.left is None and v.right is None:
            return v.val
        elif v.left is None:
            return min(self.findmin(v.right),v.val)
        elif v.right is None:
            return min(self.findmin(v.left),v.val)
        else:
            return min(self.findmin(v.left),self.findmin(v.right),v.val)
            
    def findmax(self,v):
        """find max from binary tree"""
        if v.left is None and v.right is None:
            return v.val
        elif v.left is None:
            return max(self.findmax(v.right),v.val)
        elif v.right is None:
            return max(self.findmax(v.left),v.val)
        else:
            return max(self.findmax(v.left),self.findmax(v.right),v.val)
	
	#==================
    # Naive approach  
    # Runtime : n^2 
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root.left is not None and self.findmax(root.left) >= root.val:
            return False
        if root.right is not None and self.findmin(root.right) <= root.val:
            return False
        if (self.isValidBST(root.left) == False or self.isValidBST(root.right) == False):
            return False
        return True
    
	#==================
    # Linear, with rec helper 
    def isValidBSTLinear(self,root):
        return self.isBST(root, -sys.maxsize, sys.maxsize)

    def isBST(self, root, mi, ma):
    	if root is None:
    		return True 
    	if root.val < mi or root.val > ma:
    		return False
    	return self.isBST(root.left, mi, root.val) and self.isBST(root.right, root.val, ma)


	#==================
    # Linear, without rec helper
    def isValidBSTLinear2(self,root):
        if root is None:
        	return None, None, True 
        if root.left is None and root.right is None:
        	return root.val, root.val, True

        lmin = sys.maxsize
        rmin = sys.maxsize
        lmax = -sys.maxsize
        rmax = -sys.maxsize

        if root.left is not None:
       		lmin, lmax, lbool = self.isValidBSTLinear2(root.left)
       		if root.val < lmax:
       			lbool = False
       		lmin = min(root.val, lmin)
       		lmax = max(root.val, lmax)
       		# print(root.val, lmin, lmax,lbool)
       	if root.right is not None:
       		rmin, rmax, rbool = self.isValidBSTLinear2(root.right)
       		if root.val > rmin:
       			rbool = False
       		rmin = min(root.val, rmin)
       		rmax = max(root.val, rmax)
       		# print(root.val,rmin,rmax,rbool)       
        return min(lmin,rmin), max(lmax,rmax), lbool and rbool


s = Solution()

t1 = TreeNode(5,TreeNode(1),TreeNode(6))
t2 = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6))
t3 = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(6)),TreeNode(6))
testlist = [t1,t2,t3]
for t in testlist:
	print(s.isValidBSTLinear2(t))

