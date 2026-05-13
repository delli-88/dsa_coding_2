class Node:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if curr.links[idx] is None:
                curr.links[idx] = Node()

            curr = curr.links[idx]

        curr.flag = True

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.root)

    def dfs(self, word, i, node):

        if i == len(word):
            return node.flag

        ch = word[i]

        # normal character
        if ch != ".":
            idx = ord(ch) - ord("a")

            if node.links[idx] is None:
                return False

            return self.dfs(word, i + 1, node.links[idx])

        # wildcard '.'
        else:
            for child in node.links:
                if child and self.dfs(word, i + 1, child):
                    return True

            return False