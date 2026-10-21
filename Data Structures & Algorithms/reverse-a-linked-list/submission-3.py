# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        prevNode = None
        currNode = head
        nextNode = head.next
        # print(type(nextNode))

        while nextNode:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
        # print(prevNode.val, currNode.val, nextNode)
        currNode.next = prevNode
            
        return currNode