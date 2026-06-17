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
        mappedCopy = {None: None}

        node = head
        while node:
            copy = Node(node.val)
            mappedCopy[node] = copy
            node = node.next

        node = head
        while node:
            copy = mappedCopy[node]
            copy.next = mappedCopy[node.next]
            copy.random = mappedCopy[node.random]
            node = node.next

        return mappedCopy[head]