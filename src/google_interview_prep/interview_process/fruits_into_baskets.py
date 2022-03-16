from typing import List


# NOTE: This is a good sliding window problem that isn't a string one
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # fruits[i] ~ type of fruit that the ith tree produces
        # collect as many fruits as possible
        # You only have two baskets, and each basket can only hold a single type of fruit.
        # Starting from any tree of your choice, you must pick exactly one fruit from every tree
        # while moving to the right. The picked fruits must fit in one of your baskets.
        # Once you reach a tree with fruit that cannot fit in your baskets, you must stop

        # The idea here is that there exist some subarray within the fruits array
        # that only has 2 unique items.
        # we should keep track of such a unique subarray
        # one way we can do this is via a sliding window
        counter, start, end = {}, 0, 0

        while end < len(fruits):
            val = fruits[end]
            counter[val] = counter.get(val, 0) + 1
            if len(counter) > 2:
                counter[fruits[start]] -= 1
                if counter[fruits[start]] == 0:
                    del counter[fruits[start]]
                start += 1

            end += 1

        return end - start

    # Since BF algo is already O(n^2), then we should
    # optimize for O(n)
    def brute_force(self, fruits: List[int]) -> int:
        max_fruits = 0

        for i in range(len(fruits)):
            num_unique = 0
            count = 0
            seen = set()
            for j in range(i, len(fruits)):
                if fruits[j] not in seen:
                    if num_unique == 2:
                        break

                    num_unique += 1
                    seen.add(fruits[j])
                count += 1

            max_fruits = max(max_fruits, count)

        return max_fruits

