# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
       temp=head.next
       prev=head
       critical_points=0
       ans=[]
       i=0
       while temp is not None:
        i+=1
        if prev is not None and temp.next is not None:
            if (temp.val>prev.val and temp.val>temp.next.val) or (temp.val<prev.val and temp.val<temp.next.val):
                critical_points+=1
                ans.append(i)
        temp=temp.next
        prev=prev.next
       if critical_points<2:
            return [-1,-1]
       minimum=float('inf')
       j=0
       k=1
       while k<len(ans):
           l=ans[k]-ans[j]
           if l<minimum:
              minimum=l
           j+=1
           k+=1
       return [minimum,ans[-1]-ans[0]]
        