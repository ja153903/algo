from ...src.google.lp1146 import SnapshotArray


def test_lp1146_case1():
    # ["SnapshotArray","set","snap","snap","get","get","snap","snap"]
    # [[2],[0,12],[],[],[1,0],[1,0],[],[]]
    arr = SnapshotArray(2)
    arr.set(0, 12)

    assert arr.snap() == 0
    assert arr.snap() == 1

    assert arr.get(1, 0) == 0
    assert arr.get(1, 0) == 0

    assert arr.snap() == 2
    assert arr.snap() == 3


def test_lp1146_case2():
    # ["SnapshotArray","set","snap","set","get"]
    # [[3],[0,5],[],[0,6],[0,0]]
    arr = SnapshotArray(3)

    arr.set(0, 5)

    assert arr.snap() == 0

    arr.set(0, 6)

    assert arr.get(0, 0) == 5
