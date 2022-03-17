class Solution:
    def reorderSpaces(self, text: str) -> str:
        """
        Find the number of spaces
        Find the words
        """
        words = text.split()
        spaces = text.count(" ")

        if len(words) == 1:
            return words[0] + " " * spaces

        spaces_between = spaces // (len(words) - 1)
        rem = spaces % (len(words) - 1)

        spacer = " " * spaces_between

        return spacer.join(words) + (" " * rem)
