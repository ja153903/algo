from dataclasses import dataclass
from collections import defaultdict


"""
In terms of storing snapshots, the key will be the index
of the array and the value should be the a list of objects
that contain the value and the snap_id
"""


@dataclass
class SnapshotNode:
    val: int
    snap_id: int


class SnapshotArray:
    def __init__(self, length: int):
        # key is the index, value is a list of SnapshotNodes
        self.snapshots = defaultdict(list)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if (
            index in self.snapshots
            and self.snapshots[index][-1].snap_id == self.snap_id
        ):
            self.snapshots[index][-1].val = val
        else:
            self.snapshots[index].append(SnapshotNode(val, self.snap_id))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        values_at_index = self.snapshots.get(index)
        if not values_at_index:
            return 0

        # these are sorted nodes.
        left, right = 0, len(values_at_index) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            # this condition makes sure that we get the largest snap_id
            # less than the target snap_id
            if values_at_index[mid].snap_id <= snap_id:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        if answer == -1:
            return 0

        return values_at_index[answer].val
