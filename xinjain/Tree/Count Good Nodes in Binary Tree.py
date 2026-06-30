Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 定义递归函数：current_max 是路径上的最大值
        def dfs(node, current_max):
            # 递归终止条件：空节点返回 0
            if not node:
                return 0

            count = 0
            # 判断当前节点是否是好节点
            if node.val >= current_max:
                count = 1
                # 更新路径最大值
                current_max = node.val

            # 递归左子树 + 递归右子树 + 当前节点的计数
            return count + dfs(node.left, current_max) + dfs(node.right, current_max)

        # 初始调用：根节点的路径最大值就是它自己
        return dfs(root, float('-inf'))
        # -inf表示负无穷