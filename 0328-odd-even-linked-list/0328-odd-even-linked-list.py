# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        arr=[]
        temp=head
        if head==None:
            return head
        while temp is not None:
            arr.append(temp.val)
            if temp.next is None:
                temp=None
            else:
                temp=temp.next.next
        temp=head.next
        while temp is not None:
            arr.append(temp.val)
            if temp.next is None:
                temp=None
            else:
                temp=temp.next.next
        temp=head
        i=0
        while temp is not None:
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head