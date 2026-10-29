"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}

        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next
        
        for old, new in copies.items():
            if old.next == None:
                new.next = None
                continue
            new.next = copies[old.next]
        
        for old, new in copies.items():
            if old.random == None:
                new.random = None
                continue
            new.random = copies[old.random]
        return copies[head] if head else head
        