class TrieNode:
    def __init__(self):
        self.children={}
        self.prefixCount=0
        self.wordCount=0
class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
            curr.prefixCount=curr.prefixCount+1
        curr.wordCount=curr.wordCount+1

    def countWordsEqualTo(self, word: str) -> int:
        curr=self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
            else:
                return 0
        return curr.wordCount
            
    def countWordsStartingWith(self, prefix: str) -> int:
        curr=self.root
        for c in prefix:
            if c in curr.children:
                curr=curr.children[c]
            else:
                return 0
        return curr.prefixCount

    
    def erase(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
                curr.prefixCount=curr.prefixCount-1
            else:
                return 
        curr.wordCount=curr.wordCount-1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)