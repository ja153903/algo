from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        sb = []

        for s in strs:
            n = len(s)
            sb.append(f'{n}/{s}')

        return "".join(sb)

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i < len(s):
            # Find the index of the slash starting from i
            slash = s.find('/', i)
            # This parses the size of the string
            size = int(s[i: slash])

            # update i to the next value
            i = slash + size + 1

            # store the result from post slash to next value
            result.append(s[slash + 1 : i])

        return result
