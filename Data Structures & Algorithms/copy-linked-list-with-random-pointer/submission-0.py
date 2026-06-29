"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        hm[None] = None

        curr1 = head
        anchor = curr2 = Node(0)
        while curr1:
            newCurr = None
            newNext = None
            newRandom = None

            if curr1 in hm:
                newCurr = hm[curr1]
            else:
                newCurr = Node(0)
                hm[curr1] = newCurr

            if curr1.next in hm:
                newNext = hm[curr1.next]
            else:
                newNext = Node(0)
                hm[curr1.next] = newNext

            if curr1.random in hm:
                newRandom = hm[curr1.random]
            else:
                newRandom = Node(0)
                hm[curr1.random] = newRandom

            newCurr.val = curr1.val
            newCurr.next = newNext
            newCurr.random = newRandom

            curr1 = curr1.next
            curr2.next = newCurr
            curr2 = newCurr
        return anchor.next
