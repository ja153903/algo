"""
Template for sliding window questions with strings
"""
from typing import List
from collections import Counter


def sliding_window(s: str, t: str) -> str:
    counter = Counter(t)
    target = len(t)
    min_window = ""

    start = 0

    for end in range(len(s)):
        # If value exists within the map, decrement target
        if counter.get(s[end], 0) > 0:
            target -= 1

        counter[s[end]] -= 1

        # if we've achieved the substring, then we need to update the start
        while target == 0:
            current_window_length = end - start + 1

            if not min_window or len(min_window) > current_window_length:
                min_window = s[start : end + 1]

            counter[s[start]] += 1

            if counter[s[start]] > 0:
                target += 1

        return min_window


# this solve a max subarray problem for k elements
def sliding_window_for_k_elements(items: List[int], k: int) -> int:
    counter, start = {}, 0
    maxlen = 0

    for end, value in enumerate(items):
        counter[value] = counter.get(value, 0) + 1

        if len(counter) > k:
            counter[items[start]] -= 1
            if counter[items[start]] == 0:
                del counter[items[start]]

            start += 1

        maxlen = max(maxlen, end - start + 1)

    return maxlen
