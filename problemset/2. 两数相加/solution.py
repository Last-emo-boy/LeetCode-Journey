class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.addLists(l1, l2, 0)

    def addLists(self, l1, l2, carry):
        if not l1 and not l2:
            if carry > 0:
                return ListNode(carry)
            else:
                return None

        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum_val = val1 + val2 + carry
        digit = sum_val % 10
        carry = sum_val // 10

        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None

        node = ListNode(digit)
        node.next = self.addLists(next1, next2, carry)

        return node