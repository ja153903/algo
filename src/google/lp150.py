from typing import List


"""
Evaluate Reverse Polish Notation

tokens = ["2","1","+","3","*"]

tokens.pop() => *

if we have an operation, we should look at the next two elements.
If both of the next two elements are numbers, then we evaluate

"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['*', '+', '-', '/'])
        stack = []

        for token in tokens:
            if token in operators:
                m = stack.pop()
                n = stack.pop()
                stack.append(self.eval(token, m, n))
            else:
                stack.append(int(token))

        return stack[-1]

    def eval(self, operator: str, m: int, n: int) -> int:
        if operator == '+':
            return n + m
        elif operator == '-':
            return n - m
        elif operator == '/':
            return int(float(n) / m)
        else:
            return n * m

