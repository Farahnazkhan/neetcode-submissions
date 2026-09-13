# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if not head.next:
            return False
        fast = head.next.next

        while slow and fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True
        return False
        


        