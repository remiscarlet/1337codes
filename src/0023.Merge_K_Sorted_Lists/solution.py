from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Runtime: 61.22%
    Memory: 92.42%
    """

    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]

        def mergeLists(l1: ListNode, l2: ListNode) -> ListNode:
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

        def helper(lists_to_merge: List[ListNode]) -> ListNode:
            lists_count = len(lists_to_merge)
            if lists_count == 1:
                return lists_to_merge[0]
            elif lists_count == 2:
                return mergeLists(lists_to_merge[0], lists_to_merge[1])
            else:
                mid = lists_count // 2
                return mergeLists(
                    helper(lists_to_merge[:mid]), helper(lists_to_merge[mid:])
                )

        return helper(lists)
