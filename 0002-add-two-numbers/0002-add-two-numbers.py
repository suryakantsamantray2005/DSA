class Solution:
    def addTwoNumbers(self, l1, l2):
        tempA=l1
        tempB=l2
        dummy=ListNode(0)
        temp=dummy
        carry=0
        while tempA is not None or tempB is not None:
            valA=tempA.val if tempA is not None else 0
            valB=tempB.val if tempB is not None else 0
            total_val=valA+valB+carry
            if total_val<10:
                temp.next=ListNode(total_val)
                temp=temp.next
                carry=0
            else:
                val=total_val%10
                carry=1
                temp.next=ListNode(val)
                temp=temp.next
            if tempA is not None:
                tempA=tempA.next
            if tempB is not None:
                tempB=tempB.next
            if carry==1:
                temp.next=ListNode(carry)
        return dummy.next