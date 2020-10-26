'''
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.
For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" 
and indexes = [0, 2, 5].
Then for each index, we will recover the word by reading from the reference string from 
that index until we reach a "#" character.
What is the length of the shortest reference string S possible that encodes the given words?

Example:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Note:
- 1 <= words.length <= 2000.
- 1 <= words[i].length <= 7.
- Each word has only lowercase letters.
'''
from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        S = set(words)
        ans = 0
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in S:
                    S.discard(word[i:])

        return sum([len(word)+1 for word in S])

    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        words = sorted(words, key=lambda word: len(word), reverse=True)
        ans = 0
        for word in words:
            ans += trie.insert(word[::-1])
        return ans

class TrieNode:
    def __init__(self):
        self.data = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        isNewWord = False
        for c in word:
            if c not in node.data:
                isNewWord = True
                node.data[c] = TrieNode()
            node = node.data[c]
        return len(word) + 1 if isNewWord else 0

print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
print(Solution().minimumLengthEncoding(["me", "time"]))

