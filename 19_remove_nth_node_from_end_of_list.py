class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        ptr = head

        while ptr:
            counter += 1
            ptr = ptr.next

        if counter == 1:
            return None

        counter -= n
        if counter == 0:
            return head.next
        ptr = head
        
        while counter > 1:
            ptr = ptr.next
            counter -= 1

        ptr.next = ptr.next.next

        return head
