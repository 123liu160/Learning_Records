# 给你一棵 二叉搜索树（BST） 和一个整数 k。
# 返回树中 第 k 小的元素（从 1 开始数）。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 用于存放结果和计数
        self.count = 0
        self.res = None

        def inorder(node):
            if not node:
                return

            # 1. 左子树
            inorder(node.left)

            # 2. 根节点（开始计数）
            self.count += 1
            if self.count == k:
                self.res = node.val
                return

            # 3. 右子树
            inorder(node.right)

        inorder(root)
        return self.res

    # 二叉搜索树（BST）找第k小
    # 一定用中序遍历：左 → 根 → 右
    # 遍历结果天然从小到大数到第k个，就是答案