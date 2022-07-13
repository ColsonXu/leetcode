class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # partitioning
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing right half
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # combining
        l, r = head, prev
        while r:
            tmp1 = l.next
            l.next = r
            tmp2 = r.next
            r.next = tmp1
            l = tmp1
            r = tmp2

