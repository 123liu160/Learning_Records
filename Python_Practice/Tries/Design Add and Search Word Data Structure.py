# 设计一个数据结构，支持添加新单词和查找已有单词。
# 实现 WordDictionary 类：
# void addWord(word)：将单词加入该数据结构。
# bool search(word)：如果数据结构中存在任意字符串能匹配传入的单词则返回 true，否则返回 false。
# 搜索单词中可能包含点号 .，点号可以匹配任意一个字母。
class WordDictionary:

    def __init__(self):
        # 自身作为Trie节点，26个小写字母
        self.children = [None] * 26
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = WordDictionary()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            # 遍历到单词末尾，判断是否是完整单词
            if idx == len(word):
                return node.is_end
            ch = word[idx]
            if ch == '.':
                # 通配符，遍历所有存在的子节点递归查找
                for child in node.children:
                    if child and dfs(child, idx + 1):
                        return True
                return False
            else:
                # 普通字母，走对应子节点
                pos = ord(ch) - ord('a')
                if not node.children[pos]:
                    return False
                return dfs(node.children[pos], idx + 1)

        return dfs(self, 0)