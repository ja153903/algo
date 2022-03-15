from ...src.google.lp833 import Solution


solution = Solution()


def test_lp833_case1():
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]

    expected = "eeebffff"

    assert solution.findReplaceString(s, indices, sources, targets) == expected


def test_lp833_case2():
    s = "abcd"
    indices = [0, 2]
    sources = ["ab", "ec"]
    targets = ["eee", "ffff"]

    expected = "eeecd"

    assert solution.findReplaceString(s, indices, sources, targets) == expected


def test_lp833_case3():
    s = "vmokgggqzp"
    indices = [3,5,1]
    sources = ["kg","ggq","mo"]
    targets = ["s","so","bfr"]

    expected = "vbfrssozp"

    assert solution.findReplaceString(s, indices, sources, targets) == expected
