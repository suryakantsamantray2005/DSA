# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        visit=set()
        temp=headA
        while temp is not None:
            visit.add(temp)
            temp=temp.next
        temp=headB
        while temp is not None:
            if temp in visit:
                return temp
            else:
                temp=temp.next