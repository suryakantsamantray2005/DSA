# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        visited={}
        i=head
        while i is not None:
            if i in visited:
                return True
            else:
                visited[i]=1
            i=i.next
        return False