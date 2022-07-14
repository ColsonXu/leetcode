class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        
        return False
