from typing import Dict
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    has_word: bool = False
    children: Dict[str, "TrieNode"] = field(default_factory=dict)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
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
