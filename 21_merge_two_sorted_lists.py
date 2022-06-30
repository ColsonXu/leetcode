class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        current = res
        while list1 and list2:
            t1, t2 = list1, list2
            if t1.val < t2.val:
                list1 = list1.next
                current.next = t1
            else:
                list2 = list2.next
                current.next = t2
            current = current.next

        current.next = list1 if list1 else list2

        return res.next
