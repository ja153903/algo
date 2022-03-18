"""
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

leetcode.com => google.com => facebook.com => youtube.com

back(1) => facebook.com
back(1) => google.com
forward(1) => facebook.com
visit(linkedin.com) => linkedin.com (we should check if the site we visit is in a set)
forward(2) => can't go anywhere since this is front of node
back(2) => google.com since one before linkedin was facebook and before that was google
back(7) => the most we can go back is 1, so we get leetcode

There are two things we need to consider here. We can keep adding these values to a stack
visited stack. We should however, keep the values we pop from the visited stack in another stack
in case we want to move forward again.

visited: leetcode => google.com => facebook.com => linkedin.com

if we hit visit and popped is not empty, then we clear popped

popped: youtube.com

note that root is never popped
"""


class BrowserHistory:
    def __init__(self, homepage: str):
        self.visited = [homepage]
        self.popped = []

    def visit(self, url: str) -> None:
        self.visited.append(url)

        if self.popped:
            self.popped.clear()

    def back(self, steps: int) -> str:
        # going back means popping from top of visited stack
        # and pushing to popped stack

        popcount = min(steps, len(self.visited) - 1)

        for _ in range(popcount):
            self.popped.append(self.visited[-1])
            self.visited.pop()

        return self.visited[-1]

    def forward(self, steps: int) -> str:
        popcount = min(steps, len(self.popped))

        for _ in range(popcount):
            self.visited.append(self.popped[-1])
            self.popped.pop()

        return self.visited[-1]
