# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev, curr = False, head
        heads = []

        while curr:
            if curr in heads:
                return True
            heads.append(curr)
            
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post

        return False
