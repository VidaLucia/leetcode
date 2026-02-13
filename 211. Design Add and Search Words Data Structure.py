class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary(object):

    def __init__(self):
        self.root= TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c,TrieNode())
        cur.isEnd = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, i):
            # reached end of word
            if i == len(word):
                return node.isEnd

            c = word[i]

            if c == '.':
                # try all possible children
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)