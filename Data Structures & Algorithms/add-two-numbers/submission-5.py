# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
    
        curr = dummy
        while l1 and l2:
            calculated = l1.val + l2.val
            if calculated // 10:
                curr.next = ListNode((calculated % 10) + carry)
                carry = 1
            else:
                curr.next = ListNode(calculated + carry)
                carry = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            calculated = l1.val + carry
            
            if calculated // 10:
                curr.next = ListNode(0)
            else:
                curr.next = ListNode(calculated)
                carry = 0
            curr = curr.next
            l1 = l1.next
        
        while l2:
            calculated = l2.val + carry
            
            if calculated // 10:
                curr.next = ListNode(0)
            else:
                curr.next = ListNode(calculated)
                carry = 0
            curr = curr.next
            l2 = l2.next

        
        if carry:
            curr.next = ListNode(1)
        
        # while dummy:
        #     print(dummy.val)
        #     dummy = dummy.next
        
        return dummy.next