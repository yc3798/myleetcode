class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node) 
        else: 
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node) 
  
def printbst(t):
    if t is not None:
        printbst(t.left)
        print(t.val)
        printbst(t.right)

def printrev(t): #back order travesal 
    h = height(t)
    if h == 0:
        print(None)
    else:
        arr = [(printlevel(h-1, t.right))[::-1], t.val, printlevel(h-1,t.left)[::-1] ]


def printlevel(h,t):
    if h == 0:
        if t is not None:
            print(t.val)
    else:
        printlevel(h-1, t.left)
        printlevel(h-1, t.right)

def height(t):
    if t is None:
        return 0
    else:
        return max(height(t.left)+1, height(t.right)+1)

  
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
  

printbst(r)
print("\n") 
printrev(r) 
print("\n")
printlevel(2,r)

print(height(r))

