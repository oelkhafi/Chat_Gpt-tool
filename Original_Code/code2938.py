class Node:
    def __init__(self):
        self.word = False
        self.children = [None] * 26

class MultiwayTrie:
    def __init__(self):
        self.root = Node()

    def _getkey(self, c):
        return ord(c) - ord('A')
        
    def _path(self, word, node):
        yield node

        for c in word:
            node = node.children[self._getkey(c)]
            if node:
                yield node
            else:
                break

    # Return True if Lexicon contains word, otherwise return False
    def find(self, word):
        path = list(self._path(word, self.root))
        return len(path) == len(word) + 1 and path[-1].word

    # Insert word into Lexicon (return nothing)
    def insert(self, word):
        path = list(self._path(word, self.root))

        for c in word[len(path) - 1:]:
            path.append(Node())
            path[-2].children[self._getkey(c)] = path[-1]

        path[-1].word = True

    # Remove word from Lexicon (return nothing)
    def remove(self, word):
        path = list(self._path(word, self.root))
        if len(path) == len(word) + 1:
            path[-1].word = False 