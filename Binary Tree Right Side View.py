# 给你一棵二叉树，返回从树的右侧看过去，能看到的节点值，按从上到下排列。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 空树直接返回空列表
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = queue.popleft()

                # 只保留每一层【最后一个】节点的值（最右侧）
                if i == level_size - 1:
                    res.append(node.val)

                # 先加左、再加右，保证从左到右遍历
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res