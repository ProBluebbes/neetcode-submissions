# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single = double = head
        while single and double:
            single = single.next
            double = double.next
            if double:
                double = double.next
            
            if single != None and single == double:
                return True

        return False