# a monotonic stack is a stack but it preserves the orders of the elements in the stack
# from left to right. For example, the monotone decreasing stack looks like:
# [5, 4, 3, 2, 1]

# If we decide to push 3 into this stack, it will pop out elements that are smaller than 3
# before 3 is pushed into the stack so after inserting 3, we get [5, 4, 3, 3]
from typing import List


def push_into_monotonic_decreasing_stack(stack: List[int], element: int) -> None:
    while stack and stack[-1] < element:
        stack.pop()
    stack.append(element)


# Given a stack [1, 2, 3, 4, 5], if we were to insert 3, we would have similar logic
# but we would pop the greater element until it's safe to insert the element specified
def push_into_monotonic_increasing_stack(stack: List[int], element: int) -> None:
    while stack and stack[-1] > element:
        stack.pop()
    stack.append(element)
