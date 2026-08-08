# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==1:
            return None
        i=1
        temp=head
        while i<(count)//2:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head
