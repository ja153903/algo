from typing import List

"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

--------
Approach
--------

Since we want to fit as many words as we can on the first line, we should then use a greedy approach
to try to fill each line with as many words as possible. We can do this by extending a pointer
to let us know up to which word is possible to include into our line
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        left = 0
        result = []

        # outer loop may skip around, but worst case, we'd go through n words O(n)
        while left < len(words):
            # determine the right pointer
            # finding the right pointer will take at worst O(n) time
            right = self.find_right(words, maxWidth, left)

            # since we're always going forward, these operations take little to no time
            result.append(self.justify(words, maxWidth, left, right))

            left = right + 1

        # O(n) time and O(n) space
        return result

    def find_right(self, words: List[str], max_width: int, left: int) -> int:
        right = left

        # to find the right
        sum = len(words[right])
        right += 1

        while right < len(words) and sum + 1 + len(words[right]) <= max_width:
            sum += 1 + len(words[right])
            right += 1

        return right - 1

    def justify(self, words: List[str], max_width: int, left: int, right: int) -> str:
        # when we're justifying this sentence, we need to know a couple things
        # we need to know how many spaces we need to include in between words
        # we also need to know how many spaces we may need to append at the end

        # if the difference between the two pointers is 0, then this means
        # that we only have 1 word on this line so we have to append the spaces
        # at the end of the word
        if right - left == 0:
            return words[left] + " " * (max_width - len(words[left]))

        # we know that we're on the last line if the right pointer is pointing
        # to the final element in the word list
        is_final_line = right == len(words) - 1

        # to find out the number of spaces that we need in between words
        # we need to know the max_width and the number of characters are in
        # the permitted number of words
        num_chars_in_range = self.words_length(words, left, right)
        num_words_in_range = right - left + 1
        num_spaces = max_width - num_chars_in_range

        num_spaces_in_between_words = num_spaces // (num_words_in_range - 1) if not is_final_line else 1

        # these spaces have to be distributed evenly
        num_spaces_to_distribute_evenly = num_spaces % (num_words_in_range - 1) if not is_final_line else 0

        builder = []

        for i in range(left, right + 1):
            builder.append(words[i])
            builder.append(" " * num_spaces_in_between_words)
            if num_spaces_to_distribute_evenly > 0:
                builder.append(" ")
                num_spaces_to_distribute_evenly -= 1

        result = "".join(builder).strip()

        curr_len = len(result)

        if curr_len < max_width:
            return result + " " * (max_width - curr_len)

        return result

    def words_length(self, words: List[str], left: int, right: int) -> int:
        length = 0
        for i in range(left, right + 1):
            length += len(words[i])

        return length
