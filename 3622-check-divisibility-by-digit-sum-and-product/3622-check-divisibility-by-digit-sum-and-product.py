class Solution:
    def checkDivisibility(self, n):
        total=0
        product=1
        temp=n
        while n!=0:
            digits=n%10
            total=total+digits
            product=product*digits
            n=n//10
        if temp%(total+product)==0:
            return True
        else:
            return False