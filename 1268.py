class TrieNode():
    def __init__(self):
        self.is_word = False
        self.data = {}
        self.count = 0 

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
        node.count += 1
    
    def search(self, word):
        node = self.root
        for c in word:
            node = node.data.get(c)
            if not node:
                return False
        return node.is_word

    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            node = node.data.get(c)
            if not node:
                return False
        return True

    
    def get_start(self, prefix):
        def _get_key(pre, pre_node):
            words_list = []
            if pre_node.is_word:
                for _ in range(pre_node.count):
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

        result = _get_key(prefix, node)
        return result[:3] if len(result) > 3 else result


class Solution:
    def suggestedProducts(self, products, searchWord):
        result = [[] for _ in range(len(searchWord))]
        products = sorted(products)

        for i in range(1, len(searchWord)+1):
            for prod in products:
                if searchWord[:i] == prod[:i] and len(result[i-1]) < 3:
                    result[i-1].append(prod)
                if len(result[i-1]) == 3:
                    break

        return result

    def suggestedProducts_v2(self, products, searchWord):
        result = []
        t = Trie()

        products.sort()
        for prod in products:
            t.insert(prod)
        
        for i in range(1, len(searchWord)+1):
            result.append(t.get_start(searchWord[:i]))

        return result


print(Solution().suggestedProducts_v2(["mobile","mobile","mouse","moneypot","monitor","mousepad"], 'mouse'))
print(Solution().suggestedProducts_v2(["havana"], 'havana'))
print(Solution().suggestedProducts_v2(["bags","baggage","banner","box","cloths"], 'bags'))
print(Solution().suggestedProducts_v2(["havana"], 'tatiana'))