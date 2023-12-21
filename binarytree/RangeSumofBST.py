# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        nums = []

        def search(node):
            if not node:
                return
            if low <= node.val and high >= node.val:
                nums.append(node.val)

            search(node.left)
            search(node.right)

            return

        search(root)

        return sum(nums)
