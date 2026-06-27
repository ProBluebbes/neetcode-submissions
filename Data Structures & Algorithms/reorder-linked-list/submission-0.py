# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 1 2 3 4 5 6

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head

        # get n
        while curr:
            n += 1
            curr = curr.next

        # get right half start
        curr = head
        rhalf = None
        i = 0
        while curr:
            i += 1
            if i > (n+1)//2:
                rhalf = curr
                break
            elif i >= n/2:
                tmp = curr.next
                curr.next = None
                curr = tmp
                continue
            
            curr = curr.next
                

        # reverse right half
        anchor = dummy = ListNode()
        curr = rhalf
        while curr:
            tmp = curr.next
            curr.next = anchor.next
            anchor.next = curr
            curr = tmp
        
        # alternate
        res = dummy = ListNode()
        curr1 = head
        curr2 = anchor.next

        while curr1 and curr2:
            dummy.next = curr1
            curr1 = curr1.next

            dummy = dummy.next
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next

        dummy.next = curr1 or curr2