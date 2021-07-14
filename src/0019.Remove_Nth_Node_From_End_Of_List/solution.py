class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 98.54%
    Memory: 91.58%
    """

    def removeNthFromEnd(self, head: "ListNode", n: int) -> "ListNode":
        cache = {}
        count = 0
        curr = head
        while True:
            cache[count] = curr

            count += 1
            curr = curr.next

            if curr is None:
                break

        target_idx = count - n

        if target_idx == 0:
            # Remove first node
            return head.next
        elif target_idx == count - 1:
            # Remove last node
            cache[target_idx - 1].next = None
            return head

        # Remove middle node
        prev_of_target = cache[target_idx - 1]
        next_of_target = cache[target_idx + 1]

        prev_of_target.next = next_of_target
        return head
