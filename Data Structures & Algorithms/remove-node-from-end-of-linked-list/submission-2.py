# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initalize left 1 step back so the space between left
        # and right is increased by 1
        dummy = ListNode(0, head)
        left = dummy

        # Get the right pointer initalized (n spaces ahead of the start)
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both up until right is None, that'll leave left 1 before the
        # element to remove
        while right:
            left = left.next
            right = right.next

        # Remove the elementing by setting next 2 steps ahead.
        left.next = left.next.next

        # Return the original head
        return dummy.next