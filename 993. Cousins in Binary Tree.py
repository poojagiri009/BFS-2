#USING DFS
#TC O(n) and SC O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None:
            return False

        self.xparent = None
        self.yparent = None
        self.xlevel = -1
        self.ylevel = -1
        self.dfs(root, 0, None, x, y)
        return (self.xparent != self.yparent and self.xlevel == self.ylevel)

    def dfs(self, root: Optional[TreeNode],level: int, parent: Optional[TreeNode],x: int, y: int) -> None:
        if root ==None or self.xparent != None and self.yparent != None:
            return
        if root.val == x:
            self.xparent = parent
            self.xlevel = level
            return
        if root.val == y:
            self.yparent = parent
            self.ylevel = level
            return
        self.dfs(root.left,level+1, root,x,y)
        self.dfs(root.right,level+1, root,x,y)






#USING BFS
#TC O(n) and SC O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root == None:
            return False
        xfound = False
        yfound = False
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get() 
                if curr.val == x:
                    xfound = True
                if curr.val == y:
                    yfound = True
                if curr.left != None and curr.right!=None:
                    if curr.left.val == x and curr.right.val == y:
                        return False
                    if curr.left.val == y and curr.right.val == x:
                        return False
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
            if xfound ==True and yfound == True:
                return True
            if xfound ==True or yfound == True:
                return False
        return False

        