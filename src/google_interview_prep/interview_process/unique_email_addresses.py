from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # each email is split between local name and domain
        # domain has no rules applied
        # periods between characters in local name should be stripped
        # everything after a plus sign in local name is ignored

        mp = {}

        for email in emails:
            local_name, domain = email.split("@")

            plus_idx = local_name.find("+")
            if plus_idx == -1:
                filtered_local_name = local_name
            else:
                filtered_local_name = local_name[:plus_idx]
            filtered_local_name = filtered_local_name.replace(".", "")

            if (filtered_local_name, domain) in mp:
                mp[(filtered_local_name, domain)] += 1
            else:
                mp[(filtered_local_name, domain)] = 1

        return len(mp)

