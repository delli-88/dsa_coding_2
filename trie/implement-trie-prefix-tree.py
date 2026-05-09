class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False
    

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:

        curr = self.root
        for i in range(len(word)):
            letterIdx = ord(word[i]) - ord("a")
            if curr.links[letterIdx] is None:
                curr.links[letterIdx] = Node()
            curr = curr.links[letterIdx]
        
        curr.flag = True


    def search(self, word: str) -> bool:

        curr = self.root

        for i in range(len(word)):
            letterIdx = ord(word[i]) - ord("a")
            if curr.links[letterIdx] is None:
                return False
            curr = curr.links[letterIdx]
        
        return curr.flag

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(len(prefix)):
            letterIdx = ord(prefix[i]) - ord("a")
            if curr.links[letterIdx] is None:
                return False
            curr = curr.links[letterIdx]
        
        return True