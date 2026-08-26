# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        temp=head 
        total_count=0
        start_head=head
        dummy=ListNode(0)
        dummy.next=head
        tail=dummy
        if head is None:
            return head
        while temp is not None:
            total_count+=1
            temp=temp.next
            tail=tail.next
        total_count=total_count
        k=k%total_count
        if k==0:
            return head
        tail.next=start_head
        desire_node_pos=total_count-k
        count=0
        temp=head
        while count<desire_node_pos-1:
            count+=1
            temp=temp.next
        head_after_rotate=temp.next
        temp.next=None
        return head_after_rotate