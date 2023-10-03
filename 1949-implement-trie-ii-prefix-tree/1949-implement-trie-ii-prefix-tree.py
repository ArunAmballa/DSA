class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.endsWith=0
        self.countPrefix=0
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
            curr.countPrefix=curr.countPrefix+1
        curr.endsWith=curr.endsWith+1
        

    def countWordsEqualTo(self, word: str) -> int:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                return 0
            curr=curr.children[index]
        return curr.endsWith

        

    def countWordsStartingWith(self, prefix: str) -> int:
        curr=self.root
        for c in prefix:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                return 0
            curr=curr.children[index]
        return curr.countPrefix
        

    def erase(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                return
            curr=curr.children[index]
            curr.countPrefix=curr.countPrefix-1
        curr.endsWith=curr.endsWith-1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)