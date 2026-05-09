class Node:
    def __init__(self):
        self.links = {}
        self.flag = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.links:
                curr.links[ch] = Node()

            curr = curr.links[ch]

        curr.flag = True


class Solution:
    def findWords(self, board, words):

        trie = Trie()

        for word in words:
            trie.insert(word)

        self.res = set()

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                self.dfs(board, r, c, trie.root, "")

        return list(self.res)

    def dfs(self, board, r, c, node, word):

        rows = len(board)
        cols = len(board[0])

        # bounds / visited
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return

        ch = board[r][c]

        if ch == "#" or ch not in node.links:
            return

        node = node.links[ch]
        word += ch

        if node.flag:
            self.res.add(word)

        # mark visited
        board[r][c] = "#"

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        for dr, dc in dirs:
            self.dfs(board, r + dr, c + dc, node, word)

        # backtrack
        board[r][c] = ch