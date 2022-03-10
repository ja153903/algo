from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional['ListNode'] = None

