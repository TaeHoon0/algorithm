# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:
    # bfs
    def serialize(self, root):
        if not root:
            return "null"

        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                res.append(str(node.val))   # root의 val 저장
                queue.append(node.left)     # queue에 left 저장
                queue.append(node.right)
            else:
                res.append("null")

        print(res)
        return ",".join(res)

    def deserialize(self, data):
        if not data or data == "null":
            return None

        values = data.split(',')  # data는 직렬화해서 문자열이므로 list로 변경
        val = values.pop(0)

        root = TreeNode(val)      # root 노드 만들기
        queue = deque([root])

        while queue and values:
            node = queue.popleft()

            left_val = values.pop(0)
            if left_val != "null":
                node.left = TreeNode(left_val)
                queue.append(node.left)

            right_val = values.pop(0)
            if right_val != "right":
                node.right = TreeNode(right_val)
                queue.append(node.right)

        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))