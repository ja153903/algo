from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left = 0
        result = []

        while left < len(words):
            right = self.find_right(left, words, maxWidth)
            result.append(self.justify(left, right, words, maxWidth))
            left = right + 1

        return result

    def find_right(self, left: int, words: List[str], max_width: int) -> int:
        right = left

        sum = len(words[right])
        right += 1

        while right < len(words) and sum + 1 + len(words[right]) <= max_width:
            sum += 1 + len(words[right])
            right += 1

        return right - 1

    def justify(self, left: int, right: int, words: List[str], max_width: int) -> str:
        if right - left == 0:
            return self.pad_result(words[left], max_width)

        is_last_line = right == (len(words) - 1)
        num_spaces = right - left
        total_space = max_width - self.words_length(left, right, words)

        space = " " if is_last_line else self.blank(total_space // num_spaces)
        remainder = 0 if is_last_line else total_space % num_spaces

        result = []

        for i in range(left, right + 1):
            result.append(words[i])
            result.append(space)
            result.append(" " if remainder > 0 else "")
            remainder -= 1

        return self.pad_result("".join(result).strip(), max_width)

    def words_length(self, left: int, right: int, words: List[str]) -> int:
        length = 0

        for i in range(left, right + 1):
            length += len(words[i])

        return length

    def pad_result(self, result: str, max_width: str) -> str:
        return result + self.blank(max_width - len(result))

    def blank(self, length: int) -> str:
        return " " * length


