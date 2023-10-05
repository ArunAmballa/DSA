class TrieNode:
    def __init__(self) -> None:
        self.children=[None]*26
        self.endOfWord=False
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                curr.children[index]=TrieNode()
            curr=curr.children[index]
        curr.endOfWord=True
    def check(self,word):
        curr=self.root
        ansString=""
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                return word
            else:
                ansString=ansString+chr(index+97)
                curr=curr.children[index]
                if curr.endOfWord==True:
                    return ansString
        return word
            
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        obj=Trie()
        for i in range(len(dictionary)):
            obj.insert(dictionary[i])
        ans=[]
        l=sentence.split()
        for i in range(len(l)):
            ans.append(obj.check(l[i]))
        print(ans)
        return " ".join(ans)


        