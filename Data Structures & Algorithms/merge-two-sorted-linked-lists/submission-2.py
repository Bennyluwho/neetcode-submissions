# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        p1 = list1
        p2 = list2

        # print(dummy.val)
        while p1 and p2:
            if p1.val < p2.val:
                dummy.next = p1
                p1 = p1.next
                dummy = dummy.next
            elif p2.val < p1.val:
                dummy.next = p2
                p2 = p2.next
                dummy = dummy.next
            else:
                dummy.next = p1
                p1 = p1.next
                dummy = dummy.next

        if p1:
            dummy.next = p1
        else:
            dummy.next = p2

        # res = res.next
        # while res:
        #     print(res.val)
        #     res = res.next

        return res.next

            

