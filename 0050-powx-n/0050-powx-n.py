class Solution:
    def myPow(self, x, n):
        ans=1
        k=n
        if n<0:
            n=-n
        while n>0:
            if n%2==0:
                x=x*x
                n=n//2
            else:
                ans=ans*x
                n=n-1
        if k<0:
            return 1/(ans)
        else:
            return ans
        