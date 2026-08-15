# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        temp=headA
        countA=0
        while temp is not None:
            countA+=1
            temp=temp.next
        temp=headB
        countB=0
        while temp is not None:
            countB+=1
            temp=temp.next
        if countA>countB:
            temp1=headB
            temp=headA
            count=0
            diff=abs(countA-countB)
            while count<diff:
                count+=1
                temp=temp.next
            while temp1!=temp:
                temp1=temp1.next
                temp=temp.next
            return temp1
        else:
            temp1=headA
            temp=headB
            count=0
            diff=abs(countA-countB)
            while count<diff:
                count+=1
                temp=temp.next
            while temp1!=temp:
                temp1=temp1.next
                temp=temp.next
            return temp1
        