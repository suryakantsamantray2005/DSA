# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        stack=[]
        temp=head
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp1=head
        while temp1 is not None:
            e=stack.pop()
            temp1.val=e
            temp1=temp1.next
        return head