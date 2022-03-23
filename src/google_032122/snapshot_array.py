from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, List


@dataclass
class SnapshotArrayNode:
    val: int
    snap_id: int


class SnapshotArray:
    capacity: int
    snap_id: int
    snapshot: DefaultDict[int, List[SnapshotArrayNode]]

    def __init__(self, length: int):
        self.capacity = length
        # key -> index
        # value -> list of snap ids
        self.snapshot = defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index in self.snapshot and self.snapshot[index][-1].snap_id == self.snap_id:
            self.snapshot[index][-1].val = val
            return

        self.snapshot[index].append(SnapshotArrayNode(val, self.snap_id))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # we want to grab the largest such answer
        values = self.snapshot.get(index)
        if not values:
            return 0

        left, right = 0, len(values) - 1
        answer = None

        while left <= right:
            mid = left + ((right - left) >> 1)

            if values[mid].snap_id <= snap_id:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        # note that we can't just do answer because 0 would turn out to be false
        # we should check that the answer is not None
        return values[answer].val if answer is not None else 0
