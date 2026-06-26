# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        
        node = head
        while node != None:
            stack.append(node.val)
            node = node.next

        node = head
        while len(stack) > 0:
            node.val = stack.pop()
            node = node.next            

        return head        