from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        # BFS to calculate the sum of each level
        level_sums = []
        queue = deque([root])
        while queue:
            level_size = len(queue) 
            level_sum = 0
            # Sum all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sums.append(level_sum)
        level_sums.sort(reverse=True)
        if k <= len(level_sums):
            return level_sums[k - 1]
        else:
            return -1
