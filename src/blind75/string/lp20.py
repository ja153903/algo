class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for ch in s:
            if ch == "(":
                stk.append(")")
            elif ch == "{":
                stk.append("}")
            elif ch == "[":
                stk.append("]")
            elif not stk or stk.pop() != ch:
                return False

        return not stk
