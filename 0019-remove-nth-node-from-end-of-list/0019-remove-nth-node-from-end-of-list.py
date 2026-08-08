# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class  Solution:
    def removeNthFromEnd(self, head, n):
        temp=head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        if count==n:
            temp=head
            head=head.next
            return head
        temp=head
        i=0
        while True:
            i+=1
            if count-i==n:
                break
            temp=temp.next
        temp.next=temp.next.next
        return head