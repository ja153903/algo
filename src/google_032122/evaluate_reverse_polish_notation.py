from typing import List


"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

--------
Approach
--------

Input: tokens = ["2","1","+","3","*"]
Output: 9

We can iterate forwards. If we see a number, we can just add them to a stack.
if we see an operation, we pop the two numbers from the top of the stack
and then evaluate and push the number back to the stack

The final value in the stack should be our solution
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # note that we're checking that the token is not in here instead of
            # checking that the token is an integer because there could be negative nums
            if token not in '*/-+':
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()

                if token == "+":
                    stack.append(n2 + n1)
                elif token == "-":
                    stack.append(n2 - n1)
                elif token == "*":
                    stack.append(n2 * n1)
                else:
                    stack.append(int(float(n2) / n1))

        return stack[-1]
