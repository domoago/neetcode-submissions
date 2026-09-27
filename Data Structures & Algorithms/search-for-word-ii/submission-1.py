class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        trie = Trie()
        visited = set()
        res = set()
        for word in words:
            trie.insert(word)
        def dfs(row, col, node, word):
            if min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visited or board[row][col] not in node.children:
                return
            node = node.children[board[row][col]]
            word += board[row][col]
            visited.add((row, col))
            if node.isWord:
                res.add(word)
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                dfs(row + dr, col + dc, node, word)
            visited.remove((row, col))
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie.root, "")
        return list(res)