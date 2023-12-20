# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def getLongestPath(root):
            nonlocal max_path

            if not root:
                return 0

            left_len = getLongestPath(root.left)        # 왼쪽 노드에서 값이 같은 노드의 길이
            right_len = getLongestPath(root.right)
            cur_left_len = cur_right_len = 0    # 현재 노드의 왼쪽, 오른쪽 길이

            if root.left and root.val == root.left.val: # 현재 노드와, 왼쪽 노드 값이 같을 때
                cur_left_len = left_len + 1
            if root.right and root.val == root.right.val:
                cur_right_len = right_len + 1

            max_path = max(max_path, cur_right_len + cur_left_len)  # 긴 값 비교

            return max(cur_left_len, cur_right_len)     # 현재 노드를 나갈 때, 긴 값 반환

        getLongestPath(root)

        return max_path
