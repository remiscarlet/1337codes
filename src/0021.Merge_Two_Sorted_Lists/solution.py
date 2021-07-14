class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 98.28%
    Memory: 61.59%
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val < l2.val:
            head = curr = l1
            l1 = l1.next
        else:
            head = curr = l2
            l2 = l2.next

        while not (l1 is None and l2 is None):
            if l1 is None:
                curr.next = l2
                break
            elif l2 is None:
                curr.next = l1
                break

            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        return head
