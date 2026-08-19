class Node:
    def __init__(self, val=None, end=False):
        self.val = val
        self.children = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        nextNode = None

        for c in word:
            nextNode = curr.children.get(c, None)
            if not nextNode:
                nextNode = Node(c)
                curr.children[c] = nextNode
            curr = nextNode
        
        if nextNode:
            nextNode.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            curr = curr.children.get(c, None)
            if not curr:
                return False
        
        if curr.end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            curr = curr.children.get(c, None)
            if not curr:
                return False
        
        return True
        
        