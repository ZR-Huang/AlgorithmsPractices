class TrieNode():
    def __init__(self):
        self.is_word = False
        self.data = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.data:
                node.data[c] = TrieNode()
            node = node.data[c]
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for c in word:
            node = node.data[c]
            if not node:
                return False
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            node = node.data[c]
            if not node:
                return False
        return True

    
    def get_start(self, prefix):
        def _get_key(pre, pre_node): # 这里的DFS写得不好，需要根据具体问题修改一下
            words_list = []
            if pre_node.is_word:
                words_list.append(pre)
            for x in pre_node.data.keys():
                words_list.extend(_get_key(pre + x, pre_node.data[x]))
            return words_list
    
        words = []
        if not self.starts_with(prefix):
            return words
        # if self.search(prefix):
        #     words.append(prefix)
        #     return words
        node = self.root
        for c in prefix:
            node = node.data[c]
        return _get_key(prefix, node)

