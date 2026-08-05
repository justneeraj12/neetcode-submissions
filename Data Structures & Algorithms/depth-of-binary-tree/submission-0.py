class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)

        return max(a,b) +1