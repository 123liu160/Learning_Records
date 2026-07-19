#给定连通无向图中的一个节点，请返回该图的深度拷贝。
#图中的每个节点包含一个整型数值，以及该节点所有相邻节点组成的列表。
#题目中的图以邻接表形式给出。邻接表是节点到邻接节点列表的映射，用于表示有限图，每一个列表对应一个节点的全部邻居。
#为方便处理：所有节点的值从 1 到 n 依次编号（n 为图中节点总数）；邻接表里节点的下标和节点自身的值一一对应，下标从 1 开始计数。
#输入的节点永远是图中第一个节点，其 val = 1。
class Solution:
    def cloneGraph(self, node):
        # 哈希表：原节点 -> 克隆节点
        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]
            # 创建当前节点副本
            clone = Node(n.val)
            visited[n] = clone
            # 遍历所有邻居，递归克隆并加入邻居列表
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        if not node:
            return None
        return dfs(node)