# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root)

    def dfs(self, root):
        queue = deque()
        rightNodes = []

        if root:
            queue.append(root)
        
        while len(queue) > 0:
            level = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == level - 1:
                    rightNodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1
        return rightNodes

            
