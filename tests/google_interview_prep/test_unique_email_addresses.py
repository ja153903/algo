from ...src.google_interview_prep.interview_process.unique_email_addresses import (
    Solution,
)


solution = Solution()


def test_unique_email_addresses_case1():
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]

    assert solution.numUniqueEmails(emails) == 2
