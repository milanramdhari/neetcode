class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.tree = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.tree
        for char in word:
            if char not in node.children: 
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True



    def search(self, word: str) -> bool:
        # use dfs to search for word and skip the "." and look at its all child

        def dfs(i, node):
            curr = node
            for i in range(i, len(word)):
                char = word[i]
                if char in curr.children:
                    curr = curr.children[char]
                elif char == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    return False
            return curr.is_end
        
        return dfs(0, self.tree)

