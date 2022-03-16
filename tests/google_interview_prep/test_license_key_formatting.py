from ...src.google_interview_prep.interview_process.license_key_formatting import Solution


solution = Solution()


def test_license_key_formatting_case1():
    s = "5F3Z-2e-9-w"
    k = 4

    assert solution.licenseKeyFormatting(s, k) == "5F3Z-2E9W"


def test_license_key_formatting_case2():
    s = "2-5g-3-J"
    k = 2

    assert solution.licenseKeyFormatting(s, k) == "2-5G-3J"
