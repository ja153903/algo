import collections


class TrieNode:
    def __init__(self) -> None:
        self.has_word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            node = node.children[ch]

        node.has_word = True

    def search(self, word: str) -> bool:
        result = self._search_word(word)
        return result and result.has_word

    def _search_word(self, word: str) -> TrieNode:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return None

            node = node.children[ch]

        return node

    def startsWith(self, prefix: str) -> bool:
        return bool(self._search_word(prefix))
