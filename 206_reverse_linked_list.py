class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1 = None
        t2 = head
        t3 = head.next
        while t3:
            t2.next = t1
            t1 = t2
            t2 = t3
            t3 = t3.next
        t2.next = t1
        return t2
            
