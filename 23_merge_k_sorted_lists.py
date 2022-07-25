class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge(l1, l2))
            lists = merged

        return lists[0]
        

    def merge(self, l1, l2):
        res = ListNode()
        curr = res

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return res.next
            
