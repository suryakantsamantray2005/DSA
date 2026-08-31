# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev=head
        temp=head.next
        i=0
        critical_points=0
        min_distance=0
        max_distance=0
        first_critical=0
        previous_critical=0
        while temp is not None:
            i+=1
            if prev is not None and temp.next is not None:
                if (temp.val>prev.val and temp.val>temp.next.val) or (temp.val<prev.val and temp.val<temp.next.val):
                    critical_points+=1
                    if critical_points==1:
                        first_critical=i
                        previous_critical=i
                    if critical_points==2:
                        min_distance=i-first_critical
                    if critical_points>1:
                        max_distance=i-first_critical
                        min_distance=min(min_distance,i-previous_critical)
                    previous_critical=i
            temp=temp.next
            prev=prev.next
        if critical_points<2:
            return [-1,-1]
        return [min_distance,max_distance]