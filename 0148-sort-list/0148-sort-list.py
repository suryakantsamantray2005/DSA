# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_array(self,left,right):
        dummy=ListNode(0)
        temp=dummy
        while left is not None and right is not None:
            if left.val<=right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        if left is not None:
            temp.next=left
        elif right is not None:
            temp.next=right
        return dummy.next
    def sortList(self,head):
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        left=head
        right=slow.next
        slow.next=None
        left_sort=self.sortList(left)
        right_sort=self.sortList(right)
        return self.merge_array(left_sort,right_sort)
        