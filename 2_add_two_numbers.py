class Solution:
    def addTwoNumbers(self, l1, l2):
        # ptr1, ptr2 = l1, l2
        # carry = 0
        # res = ListNode()
        # ptr3 = res

        # while ptr1 and ptr2:
        #     tmp = ptr1.val + ptr2.val + carry
        #     if tmp >= 10:
        #         carry = 1
        #         tmp -= 10
        #     else:
        #         carry = 0
        #     ptr3.next = ListNode(tmp)
        #     ptr1 = ptr1.next
        #     ptr2 = ptr2.next
        #     ptr3 = ptr3.next
        # 
        # while ptr1:
        #     ptr1.val += carry
        #     if ptr1.val >= 10:
        #         ptr1.val -= 10
        #     else:
        #         carry = 0
        #     ptr3.next = ptr1
        #     ptr1 = ptr1.next
        #     ptr3 = ptr3.next

        # while ptr2:
        #     ptr2.val += carry
        #     if ptr2.val >= 10:
        #         ptr2.val -= 10
        #     else:
        #         carry = 0
        #     ptr3.next = ptr2
        #     ptr2 = ptr2.next
        #     ptr3 = ptr3.next

        # if carry == 1:
        #     ptr3.next = ListNode(1)
        # 
        # return res.next
        res = ListNode()
        curr = res
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return res.next
