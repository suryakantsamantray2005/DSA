# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        slow=head
        fast=head
        temp=None
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                temp=slow
                break
        if temp==None:
            return None
        starting=head
        while starting is not None and starting.next is not None:
            if temp==starting:
                return temp
            else:
                temp=temp.next
                starting=starting.next
        return None