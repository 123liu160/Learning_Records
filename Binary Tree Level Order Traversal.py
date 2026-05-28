Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 空树直接返回空列表
        if not root:
            return []
        res = []
        # 队列初始化，存入根节点
        queue = deque([root])
        # 逐层遍历
        while queue:
            # 当前层的节点数量
            level_len = len(queue)
            cur_level = []
            # 遍历当前层所有节点
            for _ in range(level_len):
                node = queue.popleft()
                cur_level.append(node.val)
                # 左子节点入队
                if node.left:
                    queue.append(node.left)
                # 右子节点入队
                if node.right:
                    queue.append(node.right)
            # 将当前层结果加入最终列表
            res.append(cur_level)
        return res