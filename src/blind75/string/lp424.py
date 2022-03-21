from collections import Counter


"""
Problem
-------
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Approach
--------
Kadane but really confusing. Even though the solution is very short, there is actually a lot of things happening at once and it's very much worthwhile to study very closely.

key idea (1): we can find the longest repeating character with k replacement by taking the most repeated chars of that subsequence and adding k.

key idea (2): keep track of the max_count of the answer's subsequence. This refers to the most repeated char of the answer's subsequence. By updating the max_count every single time we enter the loop.

key idea (3): we can account for subsequence by removing the char at the start of the subsequence by doing count[i-max_length] -= 1. 
i-maxlength returns the char at the start of the subsequence. We don't update the max_count again here because we want max_count to only refer to the max_count of the answer's 
subsequence. Doing this trick is what allows the subsequence property to be maintained.

By only considering the count of the max_char, we don't have to keep track of which char we are actually talking about, only the max one. This allows us to ignore the distinction between AAAA and BBBB because we only care about the max_length.

You keep track of three things, the max_length of answer's string, the max_count of, and a count dict of the substring we are looking at. At the start of each loop, we add the char and find the new max_count.

If max_count + k > max_length, it means we can add another char that either the same char or a change, so max_length += 1.

If that is false, it means we haven't found a new max_count. So we need to correct the count_dict. By doing counter[i-max_length] -=1, 
we remove the char at the start of the subsequence so we can find another potential subsequence. The information about the longest string is kept in max_length.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, start = 0, 0
        counter = Counter()

        for end in range(len(s)):
            counter[s[end]] += 1

            maxf = max(maxf, counter[s[end]])
            # if the current window minus the max frequency is greater than k
            # then this means we're iterating on an invalid window so we have to
            # move the starting point to the right
            # why is this window invalid? We would need more than k replacement
            # to fill the substring with the most populated character
            if end - start + 1 - maxf > k:
                counter[s[start]] -= 1
                start += 1

        return len(s) - start
