from typing import Dict
from dataclasses import dataclass, field


@dataclass
class TrieNode:
    has_word: bool = False
    children: Dict[str, "TrieNode"] = field(default_factory=dict)


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.has_word = True

    def search(self, word: str) -> bool:
        self.has_word = False

        node = self.root
        self.dfs(node, word)

        return self.has_word

    def dfs(self, node: TrieNode, word: str) -> None:
        if not word:
            if node.has_word:
                self.has_word = True
            return

        if word[0] == ".":
            for child in node.children.values():
                self.dfs(child, word[1:])
        else:
            child = node.children.get(word[0])
            if not child:
                return

            self.dfs(child, word[1:])
