# 前缀树（又称字典树）是一种树形数据结构，用于高效存储、检索字符串集合中的关键字。该数据
# 结构的典型应用场景包括输入自动补全、拼写检查系统等。
class PrefixTree:

    def __init__(self):
        # 每个节点：26个字母子节点 + 是否单词结尾标记
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = PrefixTree()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        # 必须是完整单词末尾
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        # 前缀存在即可，不用判断结尾
        return True