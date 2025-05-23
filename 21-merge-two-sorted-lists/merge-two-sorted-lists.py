# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None :
            return
        if list1 is None and list2 is not None :
            return list2
        if list1 is not None and list2 is None :
            return list1
        
        dummyNode = ListNode(-1)
        temp = dummyNode

        while (list1 and list2) :
            if list1.val < list2.val :
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else :
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        
        if list1 is not None :
            temp.next = list1
        
        else :
            temp.next = list2
        
        return dummyNode.next