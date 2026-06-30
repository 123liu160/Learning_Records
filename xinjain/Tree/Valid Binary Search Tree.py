# 给你一棵二叉树的根节点，判断它是不是一棵有效的二叉搜索树（BST），是返回 true，不是返回 false。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            # 空节点合法
            if not node:
                return True
            # 核心判断：当前节点必须在 (low, high) 之间
            if not (low < node.val < high):
                return False
            # 左子树：最大值 = 当前节点值
            # 右子树：最小值 = 当前节点值
            # 递归判断
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        # 初始范围：负无穷 ~ 正无穷
        return dfs(root, float('-inf'), float('inf'))
#  左小右大，
# 看范围，不看爹，
# 传上下限，
# 递归判断。