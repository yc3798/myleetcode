class TreeNode(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


 def pruneSingle(t):
 	if t is None:
 		return None
 	elif t.left is None and t.right is None:
 		return t
 	elif t.left is not None and t.right is not None:
 		t.left = pruneSingle(t.left)
 		t.right = pruneSingle(t.right)
 	elif t.left is None:
 		# move t right to t
 		return t.right 
 	else: #t.right is None:
 		return t.left
 	return t

 t2 = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6))
 pruneSingle(t2)