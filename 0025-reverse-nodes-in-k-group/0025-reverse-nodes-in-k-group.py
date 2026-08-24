# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        count=0
        temp=head
        count_k=0
        group_start=head
        first_group=True
        previous_tail=head
        while temp is not None:
            count+=1
            if count==k:
                old_head=group_start
                temp1=group_start
                prev=None
                while count_k<count:
                    count_k+=1
                    front=temp1.next
                    temp1.next=prev
                    prev=temp1
                    temp1=front
                count=0
                count_k=0
                old_head.next=temp1
                group_start=temp1
                temp=temp1
                if first_group==False:
                    previous_tail.next=prev
                    previous_tail=old_head
                if first_group==True:
                    head=prev
                    first_group=False
            else:
                temp=temp.next
        return head