# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        stack = []

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        while slow:
            stack.append(slow)
            slow = slow.next
        
        # for i, node in enumerate(stack):
        #     print(i, node.val)
        
        curr = head

        while curr and stack:
            temp = stack.pop()
            if curr == temp or curr.next == temp:
                temp.next = None
                break
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next
        
        return
            
         