# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        currSorted = None
        curr1 = list1
        curr2 = list2
        
        next = chooseNext(curr1, curr2)
        if next == 1:
            currSorted = curr1
            res = currSorted
            curr1 = curr1.next
        elif next == 2:
            currSorted = curr2
            res = currSorted
            curr2 = curr2.next

        while curr1 != None or curr2 != None:
            next = chooseNext(curr1, curr2)
            if next == 1:
                currSorted.next = curr1
                currSorted = currSorted.next
                curr1 = curr1.next
            else:
                currSorted.next = curr2
                currSorted = currSorted.next
                curr2 = curr2.next

        if currSorted is not None:
            currSorted.next = None

        return res

def chooseNext(curr1, curr2):
    if curr1 is not None:
        if curr2 is not None:
            return 1 if curr1.val <= curr2.val else 2
        else:
            return 1
    else:
        if curr2 is not None:
            return 2
        else:
            return 0
        