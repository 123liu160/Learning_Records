# 给你一棵二叉搜索树（BST），所有节点值都不重复。
# 给你两个节点 p 和 q。
# 请你找到它们的最近公共祖先（LCA）。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        # 循环遍历查找
        while cur:
            # 如果当前值比p、q都大，两节点都在左子树
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            # 当前值比p、q都小，两节点都在右子树
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            # 数值分居两侧/当前就是目标节点，即为答案
            else:
                return cur
