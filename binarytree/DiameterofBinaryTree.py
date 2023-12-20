# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getDiameter(root):
            nonlocal diameter    # 함수밖의 diameter을 참조

            if not root:
                return 0

            left_depth = getDiameter(root.left)
            right_depth = getDiameter(root.right)
            print(f"root : {root}")
            print(f"left : {left_depth}, right : {right_depth}")
            diameter = max(diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1

        getDiameter(root)
        return diameter

