# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        temp=head
        if head==None:
            return head
        while temp is not None:
            if temp.next is not None:
                if temp.val==temp.next.val:
                    prev.next=temp.next
                    temp.next.prev=prev
                    temp=temp.next
                else:
                    temp=temp.next
                    prev=prev.next
            else:
                temp=temp.next
                prev=prev.next
        return dummy.next