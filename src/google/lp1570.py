from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = {i: val for i, val in enumerate(nums) if val != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        for i, val in self.v.items():
            if val == 0 or vec.v.get(i, 0) == 0:
                continue

            result += val * vec.v.get(i, 0)

        return result
