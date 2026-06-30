# 给你两个数组：
# preorder：二叉树的前序遍历
# inorder：二叉树的中序遍历
# 两个数组长度一样，没有重复数字。
# 请你重建这棵二叉树，并返回根节点。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 递归终止条件：数组空了，返回空
        if not preorder or not inorder:
            return None
        # 1. 前序第一个 = 根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        # 2. 在中序里找到根的位置，分左右
        mid = inorder.index(root_val)

        # 3. 递归建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # 4. 递归建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    # 前序定根，
    # 中序分左右，
    # 递归建完树。
    # 1.
    # 前序遍历（preorder）
    # 根 → 左 → 右
    # 第一个元素永远是根节点！
    # 2.
    # 中序遍历（inorder）
    # 左 → 根 → 右
    # 根节点左边全是左子树
    # 根节点右边全是右子树