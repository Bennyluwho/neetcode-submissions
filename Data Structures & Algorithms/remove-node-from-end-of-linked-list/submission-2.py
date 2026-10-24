# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = ListNode(-1, head)
        counter = 0

        while fast:
            if counter >= n:
                slow = slow.next
            fast = fast.next
            counter += 1
        
        if slow.val == -1:
            return slow.next.next
        
        slow.next = slow.next.next
        
        print(slow.val)
        return head


        
