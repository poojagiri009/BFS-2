#TC O(n) SC O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        q = Queue()
        result = []
        q.put(root)
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                if i == size -1 :
                    result.append(curr.val)
                if curr.left != None:
                    q.put(curr.left)
                if curr.right != None:
                    q.put(curr.right)
        return result




# USING DFS moving left first
#TC O(n) SC O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], level:int) -> None:
        if root == None:
            return []
        if level == len(self.result):
            self.result.append(root.val)
        else:
            self.result[level] = root.val
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)


# USING DFS moving right first
#TC O(n) SC O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], level:int) -> None:
        if root == None:
            return []
        if level == len(self.result):
            self.result.append(root.val)
        self.dfs(root.right, level + 1)
        self.dfs(root.left, level + 1)
    
    